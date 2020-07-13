from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import (
    MovieViewSet,
    TorrentsViewSet,
    GenreViewSet,
    CastViewSet
)

router = SimpleRouter()
router.register('', MovieViewSet, basename='movie')
router.register('genres', GenreViewSet, basename='genres')
router.register('torrents', TorrentsViewSet, basename='torrents')
router.register('cast', CastViewSet, basename='cast')

urlpatterns = router.urls
