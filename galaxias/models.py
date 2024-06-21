from django.db import models


class Galaxia(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    ubicacion = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

# Create your models here.
