from django.db import models

from personas.models import Persona
from personas.models.pelicula import Pelicula


class Calificacion(models.Model):
    valor = models.IntegerField()

    # Foreign Keys
    persona = models.ForeignKey(
        Persona,
        related_name="calificaciones",
        on_delete=models.CASCADE
    )
    pelicula = models.ForeignKey(
        Pelicula,
        related_name="calificaciones",
        on_delete=models.CASCADE
    )
