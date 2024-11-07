from django.urls import path
from .views import index,agregar_empleado, lista_empleados,login_view,logout_view
from django.contrib.auth import views as auth_views
from . import views


app_name = 'empleados'  # Define el namespace para las URLs


urlpatterns = [
    path('accounts/login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('accounts/password_change/', auth_views.PasswordChangeView.as_view(template_name='accounts/password_change.html'), name='password_change'),
    path('accounts/password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='accounts/password_change_done.html'), name='password_change_done'),


    path('', index, name='index'),  # Página de índice
    path('lista_empleados/', lista_empleados, name='lista_empleados'),
    path('agregar/', agregar_empleado, name='agregar_empleado'),
    path('lista_empleados/', lista_empleados, name='lista_empleados'),
    path('editar/<int:empleado_id>/', views.editar_empleado, name='editar_empleado'),
    path('eliminar/<int:empleado_id>/', views.eliminar_empleado, name='eliminar_empleado'),



    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),


    path('gestionar_contacto_emergencia/<int:empleado_id>/', views.gestionar_contacto_emergencia, name='gestionar_contacto_emergencia'),
    path('eliminar_contacto_emergencia/<int:contacto_id>/', views.eliminar_contacto_emergencia, name='eliminar_contacto_emergencia'),

    path('gestionar_carga_familiar/<int:empleado_id>/', views.gestionar_carga_familiar, name='gestionar_carga_familiar'),
    path('eliminar_carga_familiar/<int:carga_id>/', views.eliminar_carga_familiar, name='eliminar_carga_familiar'),


]





