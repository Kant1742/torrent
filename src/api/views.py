from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from rest_framework import status, viewsets

from requests.models import Response

from main.models import Torrents, Movie, Genre
from .serializers import (
    MovieSerializer,
    GenreSerializer,
    TorrentsSerializer,
)

def get_all_genre_titles():
    all_genres = Genre.objects.all()
    all_genres_titles = [g.title for g in all_genres]
    return all_genres_titles


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def create(self, request, *args, **kwargs):
        all_genre_titles = get_all_genre_titles()

        for i in request.data['genres']:
            if i not in all_genre_titles:
                Genre.objects.create(title=i)
                all_genre_titles = get_all_genre_titles()

        serializer = self.get_serializer(
            data=request.data, many=isinstance(request.data, list))
        serializer.is_valid()
        # serializer.is_valid(raise_exception=True)
        # serializer.save()

        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, headers=headers)
        # return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class TorrentsViewSet(viewsets.ModelViewSet):
    queryset = Torrents.objects.all()
    serializer_class = TorrentsSerializer


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
