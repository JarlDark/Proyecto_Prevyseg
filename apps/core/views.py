from django.shortcuts import render

# Create your views here.

def proyecto_home(request):
    return render(request, 'core/home.html')