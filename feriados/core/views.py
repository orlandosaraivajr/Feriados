from django.http import HttpResponse
from django.shortcuts import render

def natal(request):
    return render(request, 'natal.html')

def tiradentes(request):
    return HttpResponse('<h1>Tiradentes</h1>')