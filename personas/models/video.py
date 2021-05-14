from django.db import models

from personas.models import Persona


class Video(models.Model):
    nombre = models.CharField(max_length=200)
    personas = models.ManyToManyField(Persona, related_name="videos")
