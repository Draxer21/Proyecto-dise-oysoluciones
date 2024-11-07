from django.db import models

class Empleado(models.Model):
    # Datos personales
    nombre_completo = models.CharField(max_length=100)
    rut = models.CharField(max_length=12, unique=True)
    sexo = models.CharField(max_length=1, choices=[('M', 'Masculino'), ('F', 'Femenino')])
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20)
    
    # Datos laborales
    cargo = models.CharField(max_length=50)
    fecha_ingreso = models.DateField()
    area = models.CharField(max_length=50)
    departamento = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre_completo} - {self.rut}"


class ContactoEmergencia(models.Model):
    empleado = models.ForeignKey(Empleado,related_name='contactos_emergencia', on_delete=models.CASCADE)
    nombre_contacto = models.CharField(max_length=255)
    telefono_contacto = models.CharField(max_length=20)  # O el tipo adecuado
    relacion = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre_contacto

class CargaFamiliar(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE, related_name='cargas_familiares')
    nombre_carga = models.CharField(max_length=100)
    parentesco = models.CharField(max_length=50)
    sexo = models.CharField(max_length=1, choices=[('M', 'Masculino'), ('F', 'Femenino')])
    rut_carga = models.CharField(max_length=12)

    def __str__(self):
        return f"Carga familiar de {self.empleado.nombre_completo}"



