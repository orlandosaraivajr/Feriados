from django.http import HttpResponse

def natal(request):
    return HttpResponse("<h1><center>Não é Natal</center></h1>")