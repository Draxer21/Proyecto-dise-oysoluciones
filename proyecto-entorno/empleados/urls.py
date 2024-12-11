# empleados/urls.py
from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import EmpleadoListView, EmpleadoCreateView, EmpleadoUpdateView, EmpleadoDeleteView, EmpleadoPerfilView, EmpleadoPerfilUpdateView,CustomLoginView,enviar_mensaje_view
from .  import views

urlpatterns = [
    path('', EmpleadoListView.as_view(), name='empleado-list'),
    path('nuevo/', EmpleadoCreateView.as_view(), name='empleado-create'),
    path('editar/<int:pk>/', EmpleadoUpdateView.as_view(), name='empleado-update'),
    path('eliminar/<int:pk>/', EmpleadoDeleteView.as_view(), name='empleado-delete'),
    path('perfil/<int:pk>/', EmpleadoPerfilView.as_view(), name='empleado-perfil'),
    path('perfil/editar/', EmpleadoPerfilUpdateView.as_view(), name='empleado-perfil-editar'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('mensaje/', enviar_mensaje_view, name='enviar-mensaje'),

    # Cargas Familiares
    path('<int:empleado_id>/cargas/', views.listar_cargas_familiares, name='listar_cargas_familiares'),
    path('<int:empleado_id>/cargas/agregar/', views.agregar_carga_familiar, name='agregar_carga_familiar'),
    path('cargas/<int:carga_id>/eliminar/', views.eliminar_carga_familiar, name='eliminar_carga_familiar'),
    path('cargas/<int:carga_id>/editar/', views.editar_carga_familiar, name='editar_carga_familiar'),  # Nueva ruta


    # Contactos de Emergencia
    path('<int:empleado_id>/contactos/', views.listar_contactos_emergencia, name='listar_contactos_emergencia'),
    path('<int:empleado_id>/contactos/agregar/', views.agregar_contacto_emergencia, name='agregar_contacto_emergencia'),
    path('contactos/<int:contacto_id>/eliminar/', views.eliminar_contacto_emergencia, name='eliminar_contacto_emergencia'),




]