from django.db import models

from personas.models import Persona


class Pelicula(models.Model):
    nombre = models.CharField(max_length=200)
    director = models.CharField(max_length=200)
    sinopsis = models.CharField(max_length=500)
    anio = models.IntegerField()
