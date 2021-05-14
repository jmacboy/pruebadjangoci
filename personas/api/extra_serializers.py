from rest_framework import serializers

from personas.models import Persona, InfoContacto, Mascota, Video, Calificacion


class PersonaSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = ['id', 'nombres', 'apellidos']


class InfoContactoSerializerForPersona(serializers.ModelSerializer):
    class Meta:
        model = InfoContacto
        fields = ['id', 'email', 'telefono']


class MascotaSerializerForPersona(serializers.ModelSerializer):
    class Meta:
        model = Mascota
        fields = ['id', 'nombre', 'tipo_mascota']


class VideoSerializerForPersona(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['id', 'nombre']


class CalificacionSerializer(serializers.ModelSerializer):
    persona = PersonaSimpleSerializer(many=False)

    class Meta:
        model = Calificacion
        fields = ['id', 'valor', 'persona']
