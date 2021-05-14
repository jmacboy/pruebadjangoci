from django.conf.urls import url
from django.urls import include
from rest_framework import routers

from authentication.api import UserViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    url(r'^', include(router.urls))
]
