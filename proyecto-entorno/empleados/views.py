# empleados/views.py
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Empleado
from .forms import EmpleadoForm
from django.contrib import messages
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.models import User  
from django.contrib.auth.views import LogoutView



class EmpleadoListView(LoginRequiredMixin, ListView):
    model = Empleado
    template_name = 'empleados/empleado_list.html'
    context_object_name = 'empleados'
    login_url = 'login/'  # Redirige al inicio de sesión si no está autenticado

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser or user.is_staff:
            # Superusuarios y staff pueden ver todos los empleados
            return Empleado.objects.all()
        elif hasattr(user, 'empleado'):
            # Los empleados solo pueden ver su propio registro
            return Empleado.objects.filter(pk=user.empleado.pk)
        else:
            # Si no tiene relación con empleado, redirige
            return redirect(self.login_url)


import uuid

class EmpleadoCreateView(CreateView):
    model = Empleado
    form_class = EmpleadoForm
    template_name = 'empleados/empleado_form.html'
    success_url = reverse_lazy('empleados:lista_empleados')

    def form_valid(self, form):
        empleado = form.save(commit=False)
        username = f"{empleado.nombre_completo.lower().replace(' ', '_')}_{uuid.uuid4().hex[:6]}"
        default_password = "Cambia123"

        user = User.objects.create_user(
            username=username,
            password=default_password,
        )
        empleado.user = user
        empleado.save()

        messages.success(self.request, f"Empleado creado con éxito. Usuario: {username}")
        return super().form_valid(form)



class EmpleadoUpdateView(UpdateView):
    model = Empleado
    form_class = EmpleadoForm
    template_name = 'empleados/empleado_form.html'
    success_url = '/empleados/'

class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = 'empleados/empleado_confirm_delete.html'
    success_url = '/empleados/'

class EmpleadoPerfilView(LoginRequiredMixin, DetailView):
    model = Empleado
    template_name = 'empleados/empleado_perfil.html'
    context_object_name = 'empleado'

    def get_object(self, queryset=None):
        try:
            return Empleado.objects.get(user=self.request.user)
        except Empleado.DoesNotExist:
            messages.error(self.request, "No tienes un perfil de empleado asociado.")
            return redirect('empleado-list')

class EmpleadoPerfilUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Empleado
    form_class = EmpleadoForm
    template_name = 'empleados/empleado_form.html'
    success_url = reverse_lazy('empleado-perfil')

    def get_object(self, queryset=None):
        # Asegúrate de que el empleado solo pueda editar su propio perfil
        return Empleado.objects.get(user=self.request.user)

    def test_func(self):
        # Solo el usuario autenticado puede editar su propio perfil
        empleado = self.get_object()
        return self.request.user == empleado.user

    
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

class CustomLoginView(LoginView):
    template_name = 'empleados/login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        user = self.request.user
        if hasattr(user, 'empleado'):
            return reverse_lazy('empleado-perfil', kwargs={'pk': user.empleado.pk})
        elif user.is_superuser or user.is_staff:
            return reverse_lazy('admin:index')
        return reverse_lazy('empleado-list')


class CustomLogoutView(LogoutView):
    next_page = 'login'
    redirect_authenticated_user = True

    def get_success_url(self):
        user = self.request.user
        if hasattr(user, 'empleado'):  # Verifica si el usuario tiene un perfil de empleado asociado
            return reverse_lazy('empleado-perfil', kwargs={'pk': user.empleado.pk})
        elif user.is_superuser or user.is_staff:  # Si es admin, redirige al panel
            return reverse_lazy('admin:index')
        else:
            # Si no es un empleado ni un admin, redirige a la lista de empleados (comportamiento por defecto)
            return reverse_lazy('empleado-list')



from django.shortcuts import render

def index_view(request):
    return render(request, 'index.html')


from .forms import MensajeForm


def enviar_mensaje_view(request):
    if request.method == 'POST':
        form = MensajeForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'empleados/enviar_mensaje.html', {'form': MensajeForm(), 'success': True})
    else:
        form = MensajeForm()
    return render(request, 'empleados/enviar_mensaje.html', {'form': form})


from .models import Empleado, CargaFamiliar
from .forms import CargaFamiliarForm


def listar_cargas_familiares(request, empleado_id):
    empleado = get_object_or_404(Empleado, pk=empleado_id)
    cargas = empleado.cargas_familiares.all()
    return render(request, 'empleados/listar_cargas_familiares.html', {'empleado': empleado, 'cargas': cargas})

def agregar_carga_familiar(request, empleado_id):
    empleado = get_object_or_404(Empleado, pk=empleado_id)
    if request.method == 'POST':
        form = CargaFamiliarForm(request.POST)
        if form.is_valid():
            carga = form.save(commit=False)
            carga.empleado = empleado
            carga.save()
            return redirect('listar_cargas_familiares', empleado_id=empleado.id)
    else:
        form = CargaFamiliarForm()
    return render(request, 'empleados/agregar_carga_familiar.html', {'form': form, 'empleado': empleado})


def eliminar_carga_familiar(request, carga_id):
    carga = get_object_or_404(CargaFamiliar, pk=carga_id)
    empleado_id = carga.empleado.id
    carga.delete()
    return redirect('listar_cargas_familiares', empleado_id=empleado_id)

def editar_carga_familiar(request, carga_id):
    carga = get_object_or_404(CargaFamiliar, pk=carga_id)
    if request.method == 'POST':
        form = CargaFamiliarForm(request.POST, instance=carga)
        if form.is_valid():
            form.save()
            return redirect('listar_cargas_familiares', empleado_id=carga.empleado.id)
    else:
        form = CargaFamiliarForm(instance=carga)
    return render(request, 'empleados/editar_carga_familiar.html', {'form': form, 'carga': carga})

from .models import ContactoEmergencia
from .forms import ContactoEmergenciaForm

def listar_contactos_emergencia(request, empleado_id):
    empleado = get_object_or_404(Empleado, pk=empleado_id)
    contactos = empleado.contactos_emergencia.all()
    return render(request, 'empleados/listar_contactos_emergencia.html', {'empleado': empleado, 'contactos': contactos})

def agregar_contacto_emergencia(request, empleado_id):
    empleado = get_object_or_404(Empleado, pk=empleado_id)  # Obtiene el empleado
    if request.method == 'POST':  # Si el método es POST, procesa el formulario
        form = ContactoEmergenciaForm(request.POST)
        if form.is_valid():  # Si el formulario es válido
            contacto = form.save(commit=False)  # No guarda en la base de datos aún
            contacto.empleado = empleado  # Asocia el contacto al empleado
            contacto.save()  # Guarda el contacto
            return redirect('listar_contactos_emergencia', empleado_id=empleado.id)
    else:
        form = ContactoEmergenciaForm()  # Si no es POST, crea un formulario vacío
    return render(request, 'empleados/agregar_contacto_emergencia.html', {'form': form, 'empleado': empleado})

def eliminar_contacto_emergencia(request, contacto_id):
    contacto = get_object_or_404(ContactoEmergencia, pk=contacto_id)
    empleado_id = contacto.empleado.id
    contacto.delete()
    return redirect('listar_contactos_emergencia', empleado_id=empleado_id)

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


