from django.urls import path
from core import views

urlpatterns = [
    path('', views.proyecto_home, name='home'),
]
