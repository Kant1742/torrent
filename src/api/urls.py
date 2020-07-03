from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import (
    MovieViewSet,
    TorrentsViewSet,
    GenreViewSet,
)

router = SimpleRouter()
router.register('', MovieViewSet, basename='movie')
router.register('genres', GenreViewSet, basename='genres')
router.register('torrents', TorrentsViewSet, basename='torrents')

urlpatterns = router.urls
