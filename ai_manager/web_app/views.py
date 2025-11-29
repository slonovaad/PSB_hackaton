from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from llm.llm_bank_employee.llm_bank_employee import LlmBankEmployee
from llm.llm_lawyer.llm_lawyer import LlmLawyer
from mail_interactions.imap import take_message
from mail_interactions.cmpt import send_mail
from web_app.forms import LetterForm
from web_app.models import Sender, Letter
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
        try:
            last_mail = take_message("hacatontest@gmail.com", "izgu gpfq ipzq orkt")
            if len(last_mail) == 0:
                return render(request, "index.html", {"form": f, "is_post": False})
            author = last_mail[1]
            author = author[author.find('<') + 1:author.find('>')]
            letter = f"Тема: {last_mail[2]}\n Текст: {last_mail[3]}"

        except:
            return render(request, "index.html", {"form": f, "is_post": False})

    elif request.method == "POST":
        f = LetterForm(request.POST)
        if f.is_valid():
            author = f.data['author']
            letter = f.data['letter']
    else:
        return render(request, "index.html", {"form": f, "is_post": False})

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
        for sender in Sender.objects.filter(name=person_name, email=person_email):
            connected_senders.append(sender)
    for sender in connected_senders:
        Letter.objects.create(author=sender, text=letter)
    if len(correspondence_context) == 0:
        correspondence_context = "Предыдущая переписка отсутствует"
    res = json.loads(
        bank_employee.make_answer(author, person_info, letter, category, is_correct, comment,
                                  correspondence_context).replace('`', ''))
    context = {"deadline": res["deadline"],
               "answer": res["answer"],
               "answer_theme": res["answer_theme"],
               "is_correct": is_correct,
               "comment": comment,
               "laws": lawyer_answer["laws"],
               "person_email": person_email,
               "person_info": person_info,
               "type": category,
               "form": f,
               "author": author,
               "letter": letter,
               "is_post": True}
    return render(request, 'index.html', context)


def mail_sending(request):
    if request.method == "POST":
        email = request.POST.get("email")
        theme = request.POST.get("theme")
        text = request.POST.get("text")
        send_mail(email, theme, text)

    return HttpResponseRedirect("/", )
