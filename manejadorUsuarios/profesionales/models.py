from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    cedula = models.CharField(max_length=10)
    correo = models.CharField(max_length=50)
    fechaNacimiento = models.DateField()
    rol = models.CharField(max_length=50)
    def __str__(self):
        return "{} - {}".format(self.nombre, self.cedula)
    
class Profesional(Usuario):
    especialidad = models.CharField(max_length=50)
    def __str__(self):
        return "{} - {}".format(self.nombre, self.especialidad)
