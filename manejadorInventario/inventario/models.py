from django.db import models


# Create your models here.
class Recurso(models.Model):
    nombre = models.CharField(max_length=50)
    cantidad = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)
    proveedor = models.CharField(max_length=50)

    def __str__(self):
        return "{} - {}".format(self.nombre, self.cantidad)
