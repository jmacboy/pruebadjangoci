from django.db import models

from personas.models import Persona


class Mascota(models.Model):
    # Constants
    PERRO = 0
    GATO = 1
    LORO = 2
    LLAMA = 3
    TIPO_MASCOTA_CHOICES = [
        (PERRO, 'Perro'),
        (GATO, 'Gato'),
        (LORO, 'Loro'),
        (LLAMA, 'Llama')
    ]
    nombre = models.CharField(max_length=200, null=False)
    tipo_mascota = models.IntegerField(choices=TIPO_MASCOTA_CHOICES, default=PERRO)

    # Foreign Keys
    persona = models.ForeignKey(
        Persona,
        related_name="mascotas",
        on_delete=models.CASCADE
    )
