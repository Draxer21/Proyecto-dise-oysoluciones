# empleados/signals.py

from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from django.shortcuts import redirect
from django.urls import reverse

@receiver(user_logged_in)
def redirect_to_employees(sender, request, user, **kwargs):
    if user.is_authenticated:
        return redirect(reverse('empleados:lista_empleados'))  # Cambia esto a la URL que desees
