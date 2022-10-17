from django.http import HttpResponse
from datetime import datetime

from django.shortcuts import render
from core.models import FeriadoModel


def feriado(request):
    hoje = datetime.today()
    dia_hoje = hoje.day
    mes_hoje = hoje.month
    feriado = FeriadoModel.objects.filter(dia=dia_hoje, mes=mes_hoje)

    if feriado:
        contexto = {'feriado': True }
    else:
        contexto = {'feriado': False }
    return render(request, 'feriado.html', contexto)


def tiradentes(request):
    return HttpResponse('<h1>Tiradentes</h1>')
