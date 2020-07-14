from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from rest_framework import status, viewsets

from requests.models import Response

from main.models import Torrents, Movie, Genre, Cast, CharacterName
from .serializers import (
    MovieSerializer,
    GenreSerializer,
    TorrentsSerializer,
)

""" Commit info
Do not create the last item and only if we added a char_name
"""
def get_all_genre_titles():
    all_genres = Genre.objects.all()
    all_genres_titles = [g.title for g in all_genres]
    return all_genres_titles


def get_all_movie_slugs():
    movies = Movie.objects.all()
    movie_slugs = [m.slug for m in movies]
    return movie_slugs


def get_all_cast_names():
    all_cast = Cast.objects.all()
    all_cast_names = [c.name for c in all_cast]
    return all_cast_names


def get_all_char_names():
    all_char = CharacterName.objects.all()
    all_char_names = [c.character_name for c in all_char]
    return all_char_names


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def create(self, request, *args, **kwargs):
        # TODO optimisation, DRY, new functions

        all_genre_titles = get_all_genre_titles()
        movie_slugs = get_all_movie_slugs()
        all_cast_names = get_all_cast_names()
        all_char_names = get_all_char_names()
        # Another way of validation - MyModel.objects.filter(id__in=list_of_ids)

        requested_data = request.data
        number_of_movies = len(requested_data)

        # FIXME UNIQUE constraint failed: main_movie.slug

        # loop through all the requested_data.
        # if we have this slug then delete this movie from request
        num = 0
        while num < number_of_movies:
            if requested_data[num]["slug"] in movie_slugs:
                del requested_data[num]
                number_of_movies -= 1
            else:
                # if we don't have this slug in movie_slugs then just create  and cast
                # and we have nothing to do with request
                for i in requested_data[num]['genres']:
                    # TODO Genres.objects.filter(title__contains=i)
                    if i not in all_genre_titles:
                        Genre.objects.create(title=i)
                        all_genre_titles = get_all_genre_titles()

            # -----------------------------------------------------------------
            iteration_num = 0
            number_of_casts = len(requested_data[num]['cast'])
            for c in range(number_of_casts):
                print(c)
                if requested_data[num]['cast'][iteration_num]["name"] not in all_cast_names:
                    a = Cast.objects.create(
                        name=requested_data[num]['cast'][iteration_num]["name"],
                        url_small_image=requested_data[num]['cast'][iteration_num]['url_small_image'],
                        imdb_code=requested_data[num]['cast'][iteration_num]['imdb_code'],
                        movie=requested_data[num]['title']
                    )
                    a.character_name.create(character_name=requested_data[num]['cast'][iteration_num]['character_name'],
                                            cast=requested_data[num]['cast'][iteration_num]["name"])
                    # a.movies.update_or_create(requested_data[num]['title'])
                    # character_name__character_name=requested_data[num]['cast'][iteration_num]['character_name']
                    # CharacterName.objects.create(
                    #     character_name=requested_data[num]['cast'][iteration_num]['character_name'],
                    #     cast__name=requested_data[num]['cast'][iteration_num]['name'])
                iteration_num += 1
            # -----------------------------------------------------------------

            # cast_iteration = 0
            # # print(requested_data[num]['cast'][cast_iteration]['name'])
            # total_cast_len = len(
            #     requested_data[num]['cast'][cast_iteration])
            # while cast_iteration > total_cast_len:
            #     for c in requested_data[num]['cast'][cast_iteration]['name']:
            #         print(requested_data[num]['cast']
            #               [cast_iteration]['name'])
            #         # TODO Cast.objects.filter(name__contains=i)
            #         if c not in all_cast_names:
            #             Cast.objects.create(name=c['name'])
            #             CharacterName.objects.create(character_name=c["character_name"])
            #             all_cast_names = get_all_cast_names()
            #             all_char_names = get_all_char_names()
            #             cast_iteration += 1

            num += 1

        serializer = self.get_serializer(
            data=requested_data, many=isinstance(requested_data, list))
        serializer.is_valid(raise_exception=True)
        # serializer.is_valid()
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


class CastViewSet(viewsets.ModelViewSet):
    queryset = Cast.objects.all()
    serializer_class = GenreSerializer
