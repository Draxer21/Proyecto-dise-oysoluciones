from django.contrib import admin
from .models import Empleado, ContactoEmergencia, CargaFamiliar

admin.site.register(Empleado)
admin.site.register(ContactoEmergencia)
admin.site.register(CargaFamiliar)
