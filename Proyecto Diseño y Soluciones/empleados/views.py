from django.shortcuts import render, redirect,get_object_or_404
from .forms import EmpleadoForm, ContactoEmergenciaForm, CargaFamiliarForm
from .models import Empleado,ContactoEmergencia,CargaFamiliar
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'empleados/index.html')



def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('lista_empleados')  # Redirige a la página que desees
            else:
                form.add_error(None, "Credenciales incorrectas.")
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


from django.contrib.auth import logout

@login_required
def logout_view(request):
    logout(request)
    return redirect('accounts:login')  # Redirige a la página de login

@login_required
def agregar_empleado(request):
    if request.method == 'POST':
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_empleados')  # Redirigir a la lista de empleados
    else:
        form = EmpleadoForm()
    return render(request, 'empleados/agregar_empleado.html', {'form': form})

@login_required
def lista_empleados(request):
    empleados = Empleado.objects.all()
    return render(request, 'empleados/lista_empleados.html', {'empleados': empleados})

@login_required
def editar_empleado(request, empleado_id):
    empleado = get_object_or_404(Empleado, id=empleado_id)
    if request.method == 'POST':
        form = EmpleadoForm(request.POST, instance=empleado)
        if form.is_valid():
            form.save()
            return redirect('empleados:lista_empleados')
    else:
        form = EmpleadoForm(instance=empleado)
    return render(request, 'empleados/editar_empleado.html', {'form': form, 'empleado': empleado})

# Eliminar empleado
@login_required
def eliminar_empleado(request, empleado_id):
    empleado = get_object_or_404(Empleado, id=empleado_id)
    if request.method == 'POST':
        empleado.delete()
        return redirect('empleados:lista_empleados')
    return render(request, 'empleados/eliminar_empleado.html', {'empleado': empleado})




# Manejar contacto de emergencia
def gestionar_contacto_emergencia(request, empleado_id):
    empleado = get_object_or_404(Empleado, id=empleado_id)
    contactos = empleado.contactos_emergencia.all()  # Obtener contactos existentes

    if request.method == 'POST':
        # Obtener datos del formulario
        nombre_contacto = request.POST.get('nombre_contacto')
        telefono_contacto = request.POST.get('telefono_contacto')  # Asegúrate de que coincida
        relacion = request.POST.get('relacion')

        if nombre_contacto and telefono_contacto and relacion:  # Verificar que no sean None
            # Crear un nuevo contacto de emergencia
            ContactoEmergencia.objects.create(
                empleado=empleado,
                nombre_contacto=nombre_contacto,
                telefono_contacto=telefono_contacto,
                relacion=relacion
            )
            return redirect('empleados:gestionar_contacto_emergencia', empleado_id=empleado.id)

    # Si no es POST o si el formulario no se ha enviado correctamente
    return render(request, 'empleados/gestionar_contacto_emergencia.html', {
        'empleado': empleado,
        'contactos': contactos,
    })


def eliminar_contacto_emergencia(request, contacto_id):
    contacto = get_object_or_404(ContactoEmergencia, id=contacto_id)
    empleado_id = contacto.empleado.id
    contacto.delete()
    return redirect('empleados:gestionar_contacto_emergencia', empleado_id=empleado_id)

# Manejar carga familiar
def gestionar_carga_familiar(request, empleado_id):
    empleado = get_object_or_404(Empleado, id=empleado_id)
    cargas = empleado.cargas_familiares.all()

    if request.method == 'POST':
        # Obtener datos del formulario
        nombre_carga = request.POST.get('nombre_carga')  # Asegúrate que coincida con el modelo
        parentesco = request.POST.get('parentesco')
        sexo = request.POST.get('sexo')
        rut_carga = request.POST.get('rut_carga')

        # Verificar que todos los campos están completos
        if nombre_carga and parentesco and sexo and rut_carga:
            CargaFamiliar.objects.create(
                empleado=empleado,
                nombre_carga=nombre_carga,
                parentesco=parentesco,
                sexo=sexo,
                rut_carga=rut_carga
            )
            return redirect('empleados:gestionar_carga_familiar', empleado_id=empleado.id)
        else:
            return render(request, 'empleados/gestionar_carga_familiar.html', {
                'empleado': empleado,
                'cargas': cargas,
                'error': "Todos los campos son obligatorios."
            })

    return render(request, 'empleados/gestionar_carga_familiar.html', {
        'empleado': empleado,
        'cargas': cargas,
    })

def eliminar_carga_familiar(request, carga_id):
    carga = get_object_or_404(CargaFamiliar, id=carga_id)
    empleado_id = carga.empleado.id
    carga.delete()
    return redirect('empleados:gestionar_carga_familiar', empleado_id=empleado_id)

