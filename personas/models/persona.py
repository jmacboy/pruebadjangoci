from django.db import models


class Persona(models.Model):
    # Constants
    MASCULINO = 1
    FEMENINO = 0
    OTRO = -1
    GENERO_CHOICES = [
        (MASCULINO, 'Masculino'),
        (FEMENINO, 'Femenino'),
        (OTRO, 'Otro')
    ]

    # Attributes
    nombres = models.CharField(max_length=200)
    apellidos = models.CharField(max_length=200)
    ciudad = models.CharField(max_length=200)
    edad = models.IntegerField()
    fecha_nacimiento = models.DateField(null=True)
    genero = models.IntegerField(choices=GENERO_CHOICES, default=OTRO)


    def __str__(self):
        return self.nombres + " " + self.apellidos + " (" + str(self.id) + ")"
