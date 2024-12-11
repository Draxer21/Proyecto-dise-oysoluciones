# Generated by Django 5.1.4 on 2024-12-06 16:48

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Cargo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="Departamento",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="Area",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=100, unique=True)),
                (
                    "departamento",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="areas",
                        to="empleados.departamento",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Empleado",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre_completo", models.CharField(max_length=255)),
                ("rut", models.IntegerField(db_index=True, unique=True)),
                (
                    "digito_verificador",
                    models.CharField(default="0", max_length=1, null=True, unique=True),
                ),
                (
                    "sexo",
                    models.CharField(
                        choices=[("M", "Masculino"), ("F", "Femenino")], max_length=1
                    ),
                ),
                ("direccion", models.CharField(max_length=255)),
                ("telefono", models.CharField(max_length=20)),
                ("calle", models.CharField(default="Sin Calle", max_length=150)),
                ("numero", models.CharField(default=0, max_length=10)),
                (
                    "departamento_piso",
                    models.CharField(blank=True, max_length=50, null=True),
                ),
                (
                    "ciudad",
                    models.CharField(db_index=True, default="Santiago", max_length=100),
                ),
                (
                    "region",
                    models.CharField(
                        db_index=True, default="Región Metropolitana", max_length=100
                    ),
                ),
                ("fecha_ingreso", models.DateField(default=django.utils.timezone.now)),
                ("activo", models.BooleanField(default=True)),
                (
                    "area",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="empleados",
                        to="empleados.area",
                    ),
                ),
                (
                    "cargo",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="empleados",
                        to="empleados.cargo",
                    ),
                ),
                (
                    "departamento",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="empleados",
                        to="empleados.departamento",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ContactoEmergencia",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=255)),
                ("telefono", models.CharField(max_length=20)),
                ("relacion", models.CharField(max_length=50)),
                (
                    "empleado",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="contactos_emergencia",
                        to="empleados.empleado",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="CargaFamiliar",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=255)),
                ("parentesco", models.CharField(max_length=100)),
                (
                    "sexo",
                    models.CharField(
                        choices=[("M", "Masculino"), ("F", "Femenino")], max_length=1
                    ),
                ),
                ("rut", models.CharField(max_length=12)),
                (
                    "empleado",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="cargas_familiares",
                        to="empleados.empleado",
                    ),
                ),
            ],
        ),
    ]