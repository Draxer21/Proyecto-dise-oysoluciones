# Generated by Django 5.1.4 on 2024-12-07 02:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("empleados", "0007_alter_area_nombre_alter_cargo_nombre_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Parentesco",
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
                ("nombre", models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="Relacion",
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
                ("nombre", models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name="area",
            name="nombre",
            field=models.CharField(
                choices=[
                    ("Administrativa", "Administrativa"),
                    ("Operativa", "Operativa"),
                    ("Comercial", "Comercial"),
                ],
                max_length=100,
                unique=True,
            ),
        ),
        migrations.AlterField(
            model_name="cargo",
            name="nombre",
            field=models.CharField(
                choices=[
                    ("Analista", "Analista"),
                    ("Supervisor", "Supervisor"),
                    ("Gerente", "Gerente"),
                    ("Asistente", "Asistente"),
                ],
                max_length=100,
                unique=True,
            ),
        ),
        migrations.AlterField(
            model_name="departamento",
            name="nombre",
            field=models.CharField(
                choices=[
                    ("Recursos Humanos", "Recursos Humanos"),
                    ("Finanzas", "Finanzas"),
                    ("Operaciones", "Operaciones"),
                    ("TI", "Tecnologías de la Información"),
                ],
                max_length=100,
                unique=True,
            ),
        ),
        migrations.AlterField(
            model_name="empleado",
            name="area",
            field=models.ForeignKey(
                choices=[
                    ("Administrativa", "Administrativa"),
                    ("Operativa", "Operativa"),
                    ("Comercial", "Comercial"),
                ],
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="empleados",
                to="empleados.area",
            ),
        ),
        migrations.AlterField(
            model_name="empleado",
            name="cargo",
            field=models.ForeignKey(
                choices=[
                    ("Analista", "Analista"),
                    ("Supervisor", "Supervisor"),
                    ("Gerente", "Gerente"),
                    ("Asistente", "Asistente"),
                ],
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="empleados",
                to="empleados.cargo",
            ),
        ),
        migrations.AlterField(
            model_name="empleado",
            name="departamento",
            field=models.ForeignKey(
                choices=[
                    ("Recursos Humanos", "Recursos Humanos"),
                    ("Finanzas", "Finanzas"),
                    ("Operaciones", "Operaciones"),
                    ("TI", "Tecnologías de la Información"),
                ],
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="empleados",
                to="empleados.departamento",
            ),
        ),
        migrations.AlterField(
            model_name="empleado",
            name="digito_verificador",
            field=models.CharField(default="0", max_length=1, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name="cargafamiliar",
            name="parentesco",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="cargas_familiares",
                to="empleados.parentesco",
            ),
        ),
        migrations.AlterField(
            model_name="contactoemergencia",
            name="relacion",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="contactos",
                to="empleados.relacion",
            ),
        ),
    ]
