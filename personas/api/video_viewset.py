from rest_framework import serializers, viewsets

from personas.api import PersonaSimpleSerializer
from personas.models import Video, Persona


class VideoSerializer(serializers.ModelSerializer):
    personas = PersonaSimpleSerializer(many=True, read_only=True)
    personas_id = serializers.PrimaryKeyRelatedField(
        queryset=Persona.objects.all(),
        many=True,
        source="personas",
        write_only=True
    )

    class Meta:
        model = Video
        fields = '__all__'


class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
