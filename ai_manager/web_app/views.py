from django.shortcuts import render
from llm.llm_bank_employee.llm_bank_employee import LlmBankEmployee
from llm.llm_lawyer.llm_lawyer import LlmLawyer
from web_app.forms import LetterForm
import json


# Create your views here.
def index(request):
    query = ""
    f = LetterForm()
    author = ""
    letter = ""
    bank_employee = LlmBankEmployee()
    lawyer = LlmLawyer()
    if request.method == "GET":
        return render(request, "index.html", {"form": f, "is_post": False})
    if request.method == "POST":
        f = LetterForm(request.POST)
        if f.is_valid():
            author = f.data['author']
            letter = f.data['letter']

    category = json.loads(bank_employee.get_type(author, letter).replace('`', ''))["type"]
    lawyer_answer = json.loads(lawyer.check_correctness(author, letter, category) .replace('`', ''))
    is_correct = lawyer_answer["is_correct"]
    comment = lawyer_answer["comments"]
    person_info = lawyer_answer["person_info"]
    res = json.loads(bank_employee.make_answer(author, person_info, letter, category, is_correct, comment).replace('`', ''))
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
