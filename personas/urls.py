from django.conf.urls import url
from django.urls import include
from rest_framework import routers

from personas.api import PersonaViewSet, InfoContactoViewSet, MascotaViewSet, VideoViewSet, PeliculaViewSet

router = routers.DefaultRouter()
router.register(r'personas', PersonaViewSet)
router.register(r'infocontacto', InfoContactoViewSet)
router.register(r'mascotas', MascotaViewSet)
router.register(r'videos', VideoViewSet)
router.register(r'peliculas', PeliculaViewSet)

urlpatterns = [
    url(r'^', include(router.urls))
]
