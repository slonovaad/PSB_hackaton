from django.shortcuts import render
from llm.llm_bank_employee.llm_bank_employee import LlmBankEmployee
from llm.llm_lawyer.llm_lawyer import LlmLawyer
from mail_interactions.imap import take_message
from web_app.forms import LetterForm
from web_app.models import Sender, Letter
from mail_interactions import imap
import json


def index(request):
    """Функция для рендеринга главной страницы"""
    query = ""
    context = {}
    f = LetterForm()
    author = ""
    letter = ""
    bank_employee = LlmBankEmployee()
    lawyer = LlmLawyer()
    if request.method == "GET":
        last_mail = take_message("hacatontest@gmail.com", "izgu gpfq ipzq orkt")
        if len(last_mail) == 0:
            return render(request, "index.html", {"form": f, "is_post": False})
        author = last_mail[0][1]
        author = author[author.find('<') + 1:author.find('>')]
        letter = f"Тема: {last_mail[0][2]}\n Текст: {last_mail[0][3]}"
    if request.method == "POST":
        f = LetterForm(request.POST)
        if f.is_valid():
            author = f.data['author']
            letter = f.data['letter']

    category = json.loads(bank_employee.get_type(author, letter).replace('`', ''))["type"]
    lawyer_answer = json.loads(lawyer.check_correctness(author, letter, category).replace('`', ''))
    is_correct = lawyer_answer["is_correct"]
    comment = lawyer_answer["comments"]
    person_info = lawyer_answer["person_info"]

    person_name = lawyer_answer["person_name"]
    person_email = lawyer_answer["person_email"]
    correspondence_context = ""
    letters_count = 0
    connected_senders = []
    for sender in Sender.objects.all():
        if (sender.email == person_email and sender.email != "Undefined") or (
                sender.name == person_name and sender.name != "Неизвестно"):
            connected_senders.append(sender)
    for old_letter in Letter.objects.all():
        if old_letter.author in connected_senders:
            letters_count += 1
            correspondence_context += f"Письмо {letters_count}:\n {old_letter.text} \n"
    if len(connected_senders) == 0:
        Sender.objects.create(name=person_name, email=person_email)
        connected_senders.append(Sender.objects.get(name=person_name, email=person_email))
    for sender in connected_senders:
        Letter.objects.create(author=sender, text=letter)
    if len(correspondence_context) == 0:
        correspondence_context = "Предыдущая переписка отсутствует"
    res = json.loads(
        bank_employee.make_answer(author, person_info, letter, category, is_correct, comment,
                                  correspondence_context).replace('`', ''))
    context = {"deadline": res["deadline"],
               "answer": res["answer"],
               "is_correct": is_correct,
               "comment": comment,
               "laws": lawyer_answer["laws"],
               "person_info": person_info,
               "type": category,
               "form": f,
               "author": author,
               "letter": letter,
               "is_post": True}
    return render(request, 'index.html', context)
