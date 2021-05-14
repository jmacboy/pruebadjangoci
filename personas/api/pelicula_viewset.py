from rest_framework import serializers, viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from personas.api import CalificacionSerializer
from personas.models import Pelicula, Calificacion


class PeliculaSerializer(serializers.ModelSerializer):
    calificaciones = CalificacionSerializer(many=True)

    class Meta:
        model = Pelicula
        fields = '__all__'


class PeliculaViewSet(viewsets.ModelViewSet):
    queryset = Pelicula.objects.all()
    serializer_class = PeliculaSerializer

    @action(methods=['post'], detail=True, url_path='review', name='Add review for movie')
    def add_movie_review(self, request, pk=None):
        if pk is None:
            return Response({"detail": "movie Not found"}, status=status.HTTP_404_NOT_FOUND)
        obj_pelicula = Pelicula.objects.filter(pk=pk).first()
        if obj_pelicula is None:
            return Response({"detail": "movie Not found"}, status=status.HTTP_404_NOT_FOUND)
        if 'reviews' not in request.data:
            return Response("reviews is required", status=status.HTTP_400_BAD_REQUEST)

        reviews = request.data['reviews']
        for review in reviews:
            persona_id = review['persona_id']
            valor = review['valor']
            obj_calificacion = Calificacion()
            obj_calificacion.pelicula_id = pk
            obj_calificacion.persona_id = persona_id
            obj_calificacion.valor = valor
            obj_calificacion.save()

        obj_pelicula = Pelicula.objects.filter(pk=pk).first()
        serializer = PeliculaSerializer(obj_pelicula, many=False)
        return Response(serializer.data)
