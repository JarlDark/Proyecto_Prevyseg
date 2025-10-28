from django.urls import path
from registration import views

urlpatterns = [
    path('login/', views.proyecto_login_view, name='login'),
    path('logout/', views.proyecto_logout_view, name='logout')
]

