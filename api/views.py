from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from requests.models import Response
from rest_framework import status, viewsets

from main.models import Cast, CharacterName, Genre, Movie, Torrents
from main.services import (get_all_cast_names, get_all_char_names,
                           get_all_genre_titles, get_all_movie_slugs)
from .serializers import GenreSerializer, MovieSerializer, TorrentsSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all().prefetch_related('genres', 'cast')
    serializer_class = MovieSerializer

    def create(self, request, *args, **kwargs):
        # TODO optimisation, DRY, new functions

        # Why would I want to have these lines?
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
            print(f'views --- {num}')

            # -----------------------------------------------------------------
            iteration_num = 0
            # print(requested_data[num]['cast'])
            try:
                number_of_casts = len(requested_data[num]['cast'])

            # for c in range(number_of_casts+1): # This shit
            # if requested_data[num]['cast'][iteration_num]["name"] not in all_cast_names:
            # IndexError: list index out of range
                for c in range(number_of_casts):
                    try:
                        # if requested_data[num]['cast']:
                        if requested_data[num]['cast'][iteration_num]["name"] not in all_cast_names:
                            try:
                                a = Cast.objects.create(
                                    name=requested_data[num]['cast'][iteration_num]["name"],
                                    url_small_image=requested_data[num]['cast'][iteration_num]['url_small_image'],
                                    imdb_code=requested_data[num]['cast'][iteration_num]['imdb_code'],
                                    # movie=requested_data[num]['title']
                                )
                                a.character_name.create(
                                    character_name=requested_data[num]['cast'][iteration_num]['character_name'],
                                    cast=requested_data[num]['cast'][iteration_num]["name"]
                                )
                                a.save()
                                all_cast_names = get_all_cast_names()
                                all_char_names = get_all_char_names()
                            except KeyError:
                                print('No url_small_image')
                                a = Cast.objects.create(
                                    name=requested_data[num]['cast'][iteration_num]["name"],
                                    imdb_code=requested_data[num]['cast'][iteration_num]['imdb_code'],
                                    # movie=requested_data[num]['title']
                                )
                                a.character_name.create(
                                    character_name=requested_data[num]['cast'][iteration_num]['character_name'],
                                    cast=requested_data[num]['cast'][iteration_num]["name"]
                                )
                                a.save()
                                all_cast_names = get_all_cast_names()
                                all_char_names = get_all_char_names()
                        if requested_data[num]['cast'][iteration_num]['character_name'] not in all_char_names:
                            b = Cast.objects.get(
                                name=requested_data[num]['cast'][iteration_num]["name"])
                            b.character_name.create(
                                character_name=requested_data[num]['cast'][iteration_num]['character_name'],
                                cast=requested_data[num]['cast'][iteration_num]["name"]
                            )
                            all_char_names = get_all_char_names()
                        iteration_num += 1
                    except:
                        print('Exception inside')
            except:
                print('There is no cast')
            num += 1

        serializer = self.get_serializer(
            data=requested_data, many=isinstance(requested_data, list))
        serializer.is_valid(raise_exception=True)
        # serializer.is_valid()
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        # return Response(serializer.data, *args, **kwargs)
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
