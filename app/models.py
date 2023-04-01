from django.db import models

# Create your models here.
class Empleado(models.Model):
    nombre  = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    edad = models.IntegerField(max_length=3)
    fecha_ingreso = models.DateTimeField(auto_now_add=True)
    correo = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre + ' ' +self.apellido
