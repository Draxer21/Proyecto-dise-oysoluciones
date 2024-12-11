from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User, Group
from .models import Empleado

@receiver(post_save, sender=Empleado)
def crear_usuario_para_empleado(sender, instance, created, **kwargs):
    if created and not instance.user:
        # Generar un nombre de usuario único basado en el nombre completo y RUT
        username = f"{instance.nombre_completo.lower().replace(' ', '_')}_{instance.rut}"
        default_password = "Cambia123"  # Contraseña predeterminada

        # Crear el usuario relacionado
        user = User.objects.create_user(
            username=username,
            password=default_password,
        )

        # Asignar nombre completo al usuario
        nombres = instance.nombre_completo.split()
        user.first_name = nombres[0] if len(nombres) > 0 else ""
        user.last_name = " ".join(nombres[1:]) if len(nombres) > 1 else ""

        # Agregar al grupo "Empleados"
        empleados_group, _ = Group.objects.get_or_create(name="Empleados")
        user.groups.add(empleados_group)

        # Guardar cambios en el usuario
        user.save()

        # Vincular el usuario al empleado
        instance.user = user
        instance.save()

        print(f"Usuario creado: {username}, Contraseña: {default_password}")
