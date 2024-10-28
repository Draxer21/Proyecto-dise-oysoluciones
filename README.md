# El Correo de Yury - Sistema de Gestión de Nómina

Este sistema permite a **El Correo de Yury** gestionar eficientemente la información de los empleados, incluyendo sus datos personales, laborales, contactos de emergencia, y cargas familiares. Desarrollado en **Django**, este proyecto facilita al equipo de Recursos Humanos y a los empleados gestionar y actualizar sus datos de forma segura y confiable.

## Funcionalidades

1. **Listado de Trabajadores**: Tabla de resumen con RUT, nombre, sexo y cargo.
2. **Ficha de Trabajador**: Formulario de ingreso con datos personales, laborales, contactos de emergencia y cargas familiares.
3. **Inicio de Sesión**: Sistema de autenticación con roles para empleados y personal de RR.HH.
4. **Filtrado por RR.HH.**: Listado de trabajadores filtrable por sexo, cargo, área y departamento.
5. **Edición de Perfil de Trabajador**: Permite a los empleados actualizar su información personal, contactos y cargas familiares.
6. **Permisos**: Solo el personal autorizado puede modificar ciertos datos laborales.

## Requisitos

- Python 3.8+
- Django 4.0+
- PostgreSQL (opcional, para ambientes de producción)

## Instalación y Configuración

1. **Clonar el repositorio**:
    ```bash
    git clone https://github.com/tu_usuario/el_correo_de_yury.git
    cd el_correo_de_yury
    ```

2. **Instalar dependencias**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Configurar variables de entorno**:
    Configura las variables de entorno en `.env` siguiendo el ejemplo de `.env.example`.

4. **Migrar la base de datos**:
    ```bash
    python manage.py migrate
    ```

5. **Iniciar el servidor de desarrollo**:
    ```bash
    python manage.py runserver
    ```

## Uso

Accede al sistema en [http://localhost:8000](http://localhost:8000) y sigue las instrucciones de inicio de sesión.

## Contribuciones

Por favor, realiza pull requests con tus mejoras y abre issues para reportar problemas.

---

Este README te dará una base para documentar el proyecto, y podrás actualizarlo a medida que avancemos en el desarrollo. ¿Te gustaría empezar creando el proyecto Django y configurando el entorno en Codespaces?
