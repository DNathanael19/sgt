from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'index.html')

def saudacao(request, nome):
    return HttpResponse(f"<h1 style='color: red'>Olá {nome}</h1>")