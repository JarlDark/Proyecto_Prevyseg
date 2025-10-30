from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_cursos, name='lista_cursos'),
    path('solicitud/', views.crear_solicitud, name='crear_solicitud'),
]