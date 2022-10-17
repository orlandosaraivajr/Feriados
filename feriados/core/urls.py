from django.urls import path

from . import views


urlpatterns = [
    path('',views.feriado, name='feriado'),
    path('tiradentes',views.tiradentes, name='tiradentes'),
]
