from django.shortcuts import render
from llm.llm_main import llm_bank_employee

# Create your views here.
def index(request):
    query = request.GET.get('ask', 'Кто ты?')
    res = llm_bank_employee(query)
    context = {"answer": res}
    return render(request, 'index.html', context)