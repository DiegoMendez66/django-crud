# Generated by Django 4.1.7 on 2023-04-01 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('edad', models.IntegerField(max_length=3)),
                ('fecha_ingreso', models.DateTimeField(auto_now_add=True)),
                ('correo', models.CharField(max_length=100)),
            ],
        ),
    ]
