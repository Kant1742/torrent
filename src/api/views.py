from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from rest_framework import viewsets

from main.models import Torrents, Movie, Genre
from .serializers import (
    MovieSerializer,
    GenreSerializer,
    TorrentsSerializer,
)


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer



class TorrentsViewSet(viewsets.ModelViewSet):
    queryset = Torrents.objects.all()
    serializer_class = TorrentsSerializer


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
