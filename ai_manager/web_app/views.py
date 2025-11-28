from django.shortcuts import render
from llm.llm_main import llm_bank_employee
from web_app.forms import LetterForm
from django.shortcuts import redirect

# Create your views here.
def index(request):
    query = ""
    if request.method == "GET":
        f = LetterForm()
        query = request.GET.get('ask', 'Кто ты?')
    if request.method == "POST":
        f = LetterForm(request.POST)
        if f.is_valid():
            author = f.data['author']
            letter = f.data['letter']
            query = f"Отправитель письма: {author}\n Текст письма: {letter}"

    res = llm_bank_employee(query)
    context = {"answer": res, "form": f}
    return render(request, 'index.html', context)
