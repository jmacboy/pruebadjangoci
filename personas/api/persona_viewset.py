from rest_framework import viewsets, serializers, permissions, status
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from personas.api import InfoContactoSerializerForPersona, MascotaSerializerForPersona, VideoSerializerForPersona
from personas.models import Persona, Video


class PersonaSerializer(serializers.ModelSerializer):
    infocontacto = InfoContactoSerializerForPersona(many=False, read_only=True)
    mascotas = MascotaSerializerForPersona(many=True, read_only=True)
    videos = VideoSerializerForPersona(many=True, read_only=True)

    class Meta:
        model = Persona
        fields = '__all__'


class PersonaViewSet(viewsets.ModelViewSet):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer
    pagination_class = PageNumberPagination

    # permission_classes = [permissions.IsAuthenticated, permissions.DjangoObjectPermissions]

    @action(methods=['get'], detail=False, url_path='masculino', name='Get personas with male gender')
    def get_personas_male(self, request, pk=None):
        queryset = Persona.objects.filter(genero=Persona.MASCULINO)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        persona = serializer.instance

        if 'videos_list' in request.data:
            for video in request.data['videos_list']:
                obj_video = Video.objects.filter(pk=video).first()
                if obj_video is None:
                    return Response("video with id " + str(video) + " is invalid", status=status.HTTP_400_BAD_REQUEST)
                obj_video.personas.add(persona)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
