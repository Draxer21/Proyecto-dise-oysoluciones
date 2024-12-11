# empleados/forms.py
from django import forms
from .models import Empleado, ContactoEmergencia, CargaFamiliar,Mensaje

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = '__all__'

class ContactoEmergenciaForm(forms.ModelForm):
    class Meta:
        model = ContactoEmergencia
        fields = ['nombre', 'telefono', 'relacion']

class CargaFamiliarForm(forms.ModelForm):
    class Meta:
        model = CargaFamiliar
        fields = '__all__'

class MensajeForm(forms.ModelForm):
    class Meta:
        model = Mensaje
        fields = ['mensaje']
        widgets = {
            'mensaje': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Escribe tu mensaje aquí...', 'rows': 3}),
        }