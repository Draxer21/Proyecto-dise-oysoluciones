# Generated by Django 5.1.4 on 2024-12-07 01:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("empleados", "0004_remove_empleado_activo"),
    ]

    operations = [
        migrations.CreateModel(
            name="Ciudad",
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
                ("nombre", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Region",
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
        migrations.AlterField(
            model_name="empleado",
            name="area",
            field=models.ForeignKey(
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
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="empleados",
                to="empleados.departamento",
            ),
        ),
        migrations.AlterField(
            model_name="empleado",
            name="ciudad",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="empleados",
                to="empleados.ciudad",
            ),
        ),
        migrations.AddField(
            model_name="ciudad",
            name="region",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="ciudades",
                to="empleados.region",
            ),
        ),
        migrations.AlterField(
            model_name="empleado",
            name="region",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="empleados",
                to="empleados.region",
            ),
        ),
    ]
