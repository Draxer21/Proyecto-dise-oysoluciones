from django import forms
from .models import Empleado, ContactoEmergencia, CargaFamiliar

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ['nombre_completo', 'rut', 'sexo', 'direccion', 'telefono', 'cargo', 'fecha_ingreso', 'area', 'departamento']

class ContactoEmergenciaForm(forms.ModelForm):
    class Meta:
        model = ContactoEmergencia
        fields = ['nombre_contacto', 'relacion', 'telefono_contacto']

class CargaFamiliarForm(forms.ModelForm):
    class Meta:
        model = CargaFamiliar
        fields = ['nombre_carga', 'parentesco', 'sexo', 'rut_carga']



class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)
