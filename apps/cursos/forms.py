from django import forms
from .models import SolicitudInscripcion

class SolicitudForm(forms.ModelForm):
    class Meta:
        model = SolicitudInscripcion
        fields = ['nombre_completo', 'email', 'telefono', 'curso_interes', 'mensaje'] 
        widgets = {
            'nombre_completo': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'curso_interes': forms.Select(attrs={'class': 'form-select'}),
            'mensaje': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }