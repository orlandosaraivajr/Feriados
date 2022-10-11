from django.http import HttpResponse
from django.shortcuts import render
from core.models import FeriadoModel
from datetime import datetime

def feriado(request):
    hoje = datetime.today()
    dia_hoje = hoje.day
    mes_hoje = hoje.month
    feriado = FeriadoModel.objects.filter(dia=dia_hoje, mes=mes_hoje)
    if len(feriado) > 0:
        contexto = { 'feriado': True }
    else:
        contexto = { 'feriado': False }
    return render(request, 'feriado.html', contexto)

def tiradentes(request):
    return HttpResponse('<h1>Tiradentes</h1>')