from django.db import models
from django.contrib.auth.models import User

class Curso(models.Model):
    curso_nombre = models.CharField(max_length=100, verbose_name='Nombre')
    descripcion = models.TextField(verbose_name='Descripcion')
    duracion_horas = models.PositiveIntegerField(verbose_name='Duración en Horas')
    precio = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Precio', help_text='Precio de inscripción en CLP.')
    cupos_disponibles = models.PositiveIntegerField(default=20, verbose_name='Cupos Disponibles')
    instructor = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Instructor Asignado',
        limit_choices_to={'profile__role': 'instructor'}
    )

    def __str__(self):
        return self.curso_nombre
    
class SolicitudInscripcion(models.Model):
    ESTADO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('aprobada', 'Aprobada'),
        ('rechazada', 'Rechazada'),
    ]

    nombre_completo = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    curso_interes = models.ForeignKey(Curso, on_delete=models.SET_NULL, null=True)
    mensaje = models.TextField(blank=True, null=True)
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES, default='pendiente')
    fecha_solicitud = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Solicitud de {self.nombre_completo} - {self.estado}"