from django.contrib import admin
from django.contrib.auth.models import User
from .models import Curso, SolicitudInscripcion

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('curso_nombre', 'instructor', 'precio', 'cupos_disponibles')
    list_filter = ('instructor',)
    search_fields = ('curso_nombre', 'descripcion')

@admin.register(SolicitudInscripcion)
class SolicitudInscripcionAdmin(admin.ModelAdmin):
    list_display = ('nombre_completo', 'curso_interes', 'estado', 'fecha_solicitud')
    list_filter = ('estado', 'curso_interes')
    search_fields = ('nombre_completo', 'email')
    actions = ['aprobar_y_crear_usuario']

    def aprobar_y_crear_usuario(self, request, queryset):
        for solicitud in queryset.filter(estado='pendiente'):
            email = solicitud.email
            nombre = solicitud.nombre_completo
            
            if User.objects.filter(email=email).exists():
                self.message_user(request, f"Error: Ya existe un usuario con el correo {email}.", level='error')
                continue

            password = User.objects.make_random_password()
            user = User.objects.create_user(
                username=email, 
                email=email,
                password=password,
                first_name=nombre
            )
            solicitud.estado = 'aprobada'
            solicitud.save()
            
            print(f"Usuario Creado: {email}, Contraseña: {password}")

        self.message_user(request, "Usuarios creados y solicitudes aprobadas exitosamente.")

    aprobar_y_crear_usuario.short_description = "Aprobar solicitudes y crear cuentas de usuario"