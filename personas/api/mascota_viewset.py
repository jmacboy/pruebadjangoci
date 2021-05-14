from rest_framework import serializers, viewsets

from personas.api import PersonaSimpleSerializer
from personas.models import Mascota, Persona


class MascotaSerializer(serializers.ModelSerializer):
    persona = PersonaSimpleSerializer(many=False, read_only=True)
    persona_id = serializers.PrimaryKeyRelatedField(
        many=False, write_only=True, queryset=Persona.objects.all(),
        source='persona'
    )

    class Meta:
        model = Mascota
        fields = '__all__'


class MascotaViewSet(viewsets.ModelViewSet):
    queryset = Mascota.objects.all()
    serializer_class = MascotaSerializer
