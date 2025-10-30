from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Curso
from .forms import SolicitudForm # Importamos el formulario

def lista_cursos(request):
    cursos = Curso.objects.all()
    context = {
        'cursos': cursos
    }
    return render(request, 'cursos/lista_cursos.html', context)

def crear_solicitud(request):
    if request.method == 'POST':
        form = SolicitudForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Tu solicitud fue enviada con éxito! Te contactaremos pronto.')
            return redirect('lista_cursos')
    else:
        form = SolicitudForm()
    
    return render(request, 'cursos/crear_solicitud.html', {'form': form})