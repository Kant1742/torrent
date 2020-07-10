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
        # TODO optimisation
        movies = Movie.objects.all()
        movie_slugs = [m.slug for m in movies]
        all_genre_titles = get_all_genre_titles()

        requested_data = request.data
        number_of_movies = len(requested_data)

        # FIXME UNIQUE constraint failed: main_movie.slug

        # loop through all the requested_data.
        # if we have this slug then delete this movie from request
        # but then we have to lower our iteration number because we've just
        # deleted the previous movie and the next one took its place.
        num = 0
        while num < number_of_movies:
            if requested_data[num]["slug"] in movie_slugs:
                del requested_data[num]
                number_of_movies -= 1
                print(requested_data)
            else:
                # if we don't have this slug in movie_slugs then just create genres
                # and we have nothing to do with request
                for i in requested_data[num]['genres']:
                    if i not in all_genre_titles: # TODO Genres.objects.filter(title__contains=i)
                        Genre.objects.create(title=i)
                        all_genre_titles = get_all_genre_titles()
                num += 1

        serializer = self.get_serializer(
        data=requested_data, many=isinstance(requested_data, list))
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        # return Response(serializer.data, headers=headers)
        return Response(serializer.data, headers=headers)


class TorrentsViewSet(viewsets.ModelViewSet):
    queryset = Torrents.objects.all()
    serializer_class = TorrentsSerializer


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
