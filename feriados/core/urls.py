from django.urls import path
from . import views

urlpatterns = [
    path('',views.feriado),
    path('tiradentes',views.tiradentes),
]
