from django.contrib import admin
from .models import Empleado, CargaFamiliar, ContactoEmergencia, Mensaje  # Asegúrate de importar todos los modelos que necesitas
from .models import Relacion, Parentesco, ContactoEmergencia, CargaFamiliar

admin.site.register(Relacion)
admin.site.register(Parentesco)
admin.site.register(Empleado)
admin.site.register(CargaFamiliar)
admin.site.register(ContactoEmergencia)
admin.site.register(Mensaje)

from django.contrib import admin
from .models import Departamento, Area, Cargo, Empleado

@admin.register(Departamento)
class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ('nombre',)


@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    filter_horizontal = ('departamentos',)  # Permite seleccionar múltiples departamentos en el admin

@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')  # Muestra ID y nombre del cargo
    search_fields = ('nombre',)

