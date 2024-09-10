# Generated by Django 5.0.4 on 2024-06-19 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("los4elementos", "0005_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="estudiante",
            name="apellidos",
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name="estudiante",
            name="fecha_nacimiento",
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name="estudiante",
            name="nombre",
            field=models.CharField(max_length=200, null=True),
        ),
    ]
