from rest_framework import serializers, viewsets

from personas.api import PersonaSimpleSerializer
from personas.models import InfoContacto, Persona


class InfoContactoSerializer(serializers.ModelSerializer):
    persona = PersonaSimpleSerializer(many=False, read_only=True)
    persona_id = serializers.PrimaryKeyRelatedField(
        many=False, write_only=True, queryset=Persona.objects.all(),
        source='persona'
    )

    class Meta:
        model = InfoContacto
        fields = '__all__'


class InfoContactoViewSet(viewsets.ModelViewSet):
    queryset = InfoContacto.objects.all()
    serializer_class = InfoContactoSerializer
