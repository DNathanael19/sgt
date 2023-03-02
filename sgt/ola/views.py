from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'index.html')

#def greet(request, nome):
    #return render(request, 'greet.html', {'name':nome})

def tia_do_zap(request, nome):
    var = datetime.datetime.now()
    dia = int(var.strftime("%H"))
    boleano = bool
    if dia > 18:
        boleano = False
    else: 
        boleano = True
    return render(request, 'tia_do_zap.html', {'name':nome, 'dia': boleano})

#def saudacao(request, nome):
    #return HttpResponse(f"<h1 style='color: red'>Olá {nome}</h1>")