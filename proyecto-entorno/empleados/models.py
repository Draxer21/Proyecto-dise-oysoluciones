# empleados/models.py
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User



REGIONES_CHOICES = [
    ('Región de Arica y Parinacota', 'Región de Arica y Parinacota'),
    ('Región de Tarapacá', 'Región de Tarapacá'),
    ('Región de Antofagasta', 'Región de Antofagasta'),
    ('Región de Atacama', 'Región de Atacama'),
    ('Región de Coquimbo', 'Región de Coquimbo'),
    ('Región de Valparaíso', 'Región de Valparaíso'),
    ('Región Metropolitana de Santiago', 'Región Metropolitana de Santiago'),
    ('Región del Maule', 'Región del Maule'),
    ('Región de Ñuble', 'Región de Ñuble'),
    ('Región del Biobío', 'Región del Biobío'),
    ('Región de La Araucanía', 'Región de La Araucanía'),
    ('Región de Los Ríos', 'Región de Los Ríos'),
    ('Región de Los Lagos', 'Región de Los Lagos'),
    ('Región de Aysén', 'Región de Aysén'),
    ('Región de Magallanes y de la Antártica Chilena', 'Región de Magallanes y de la Antártica Chilena'),
]

CIUDADES_CHOICES = [
    ('Arica', 'Arica'),
    ('Iquique', 'Iquique'),
    ('Antofagasta', 'Antofagasta'),
    ('Copiapó', 'Copiapó'),
    ('La Serena', 'La Serena'),
    ('Valparaíso', 'Valparaíso'),
    ('Santiago', 'Santiago'),
    ('Talca', 'Talca'),
    ('Chillán', 'Chillán'),
    ('Concepción', 'Concepción'),
    ('Temuco', 'Temuco'),
    ('Valdivia', 'Valdivia'),
    ('Puerto Montt', 'Puerto Montt'),
    ('Coyhaique', 'Coyhaique'),
    ('Punta Arenas', 'Punta Arenas'),
]

class Departamento(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre

class Area(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    departamentos = models.ManyToManyField(Departamento, related_name='areas')

    def __str__(self):
        return self.nombre
    
class Cargo(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre
    
# empleados/models.py

class Relacion(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre

class Parentesco(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre


class Empleado(models.Model):
    # Datos personales
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='empleado', null=True, blank=True)
    nombre_completo = models.CharField(max_length=255)
    rut = models.IntegerField(unique=True, db_index=True)
    digito_verificador = models.CharField(max_length=1, unique=True, null=True, default='0')
    sexo = models.CharField(max_length=1, choices=[('M', 'Masculino'), ('F', 'Femenino')])
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20)

    # Dirección normalizada
    calle = models.CharField(max_length=150, default="Sin Calle")
    numero = models.CharField(max_length=10, default=0)
    departamento_piso = models.CharField(max_length=50, null=True, blank=True)
    ciudad = models.CharField(max_length=100, choices=CIUDADES_CHOICES, db_index=True, default="Santiago")
    region = models.CharField(max_length=100, choices=REGIONES_CHOICES, db_index=True, default="Región Metropolitana de Santiago")

    # Datos laborales
    cargo = models.ForeignKey(Cargo, on_delete=models.SET_NULL, null=True, related_name='empleados')
    fecha_ingreso = models.DateField(default=timezone.now)
    area = models.ForeignKey(Area, on_delete=models.SET_NULL, null=True, related_name='empleados')
    departamento = models.ForeignKey(Departamento, on_delete=models.SET_NULL, null=True, related_name='empleados')

    def __str__(self):
        return f"{self.nombre_completo} - {self.rut}"

    def clean(self):
        super().clean()
        # Validación de que la ciudad pertenece a la región
        # (Esto requiere que se implemente una lógica adecuada para validar)
        pass

class ContactoEmergencia(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE, related_name='contactos_emergencia')
    nombre = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20)
    relacion = models.ForeignKey(Relacion, on_delete=models.SET_NULL, null=True, related_name='contactos')

    def __str__(self):
        return f"{self.nombre} ({self.relacion})"

class CargaFamiliar(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE, related_name='cargas_familiares')
    nombre = models.CharField(max_length=255)
    parentesco = models.ForeignKey(Parentesco, on_delete=models.SET_NULL, null=True, related_name='cargas_familiares')
    sexo = models.CharField(max_length=1, choices=[('M', 'Masculino'), ('F', 'Femenino')])
    rut = models.CharField(max_length=12)

    def __str__(self):
        return f"{self.nombre} ({self.parentesco})"

    
class Mensaje(models.Model):
    mensaje = models.TextField()
    fecha_envio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Mensaje de {self.nombre} - {self.asunto}"