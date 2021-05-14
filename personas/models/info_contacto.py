from django.db import models

from personas.models import Persona


class InfoContacto(models.Model):
    email = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)

    # Foreign Keys
    persona = models.OneToOneField(
        Persona,
        related_name="infocontacto",
        on_delete=models.CASCADE
    )
