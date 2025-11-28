from django.shortcuts import render
from llm.llm_main import llm_bank_employee
from web_app.forms import LetterForm
import json


# Create your views here.
def index(request):
    query = ""
    f = LetterForm()
    author = ""
    letter = ""
    if request.method == "GET":
        # query = request.GET.get('ask', 'Кто ты?')
        return render(request, "index.html", {"form": f, "is_post": False})
    if request.method == "POST":
        f = LetterForm(request.POST)
        if f.is_valid():
            author = f.data['author']
            letter = f.data['letter']
            query = f"Отправитель письма: {author}\n Текст письма: {letter}"

    res = llm_bank_employee(query)
    res = res.replace('`', '')
    res = json.loads(res)
    context = {"deadline": res["deadline"],
               "answer": res["answer"],
               "type": res["type"],
               "form": f,
               "author": author,
               "letter": letter,
               "is_post": True}
    return render(request, 'index.html', context)
