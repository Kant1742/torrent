from rest_framework import serializers

from main.models import Movie, Genre, Torrents, Cast, CharacterName
from main.services import (
    get_all_cast_names,
    get_all_char_names,
    get_all_genre_titles,
    get_all_movie_slugs)


class TorrentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Torrents
        fields = '__all__'
        # depth = 1


class CharacterNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = CharacterName
        fields = '__all__'
        depth = 1


"""
>>> Movie.objects.filter(cast__character_name__character_name__isnull=True)
<QuerySet [<Movie: Legend>, <Movie: Legend>, <Movie: DROPtfPEDd>,
<Movie: DROPtfPEDd>, <Movie: DROPtfPEDd>, <Movie: DROPtfPEDd>]>
"""


class CastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cast
        fields = '__all__'
        depth = 1


# ----------------------------------------------------------------------------
class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    torrents = TorrentsSerializer(many=True)
    genres = serializers.SlugRelatedField(
        queryset=Genre.objects.all(), many=True, slug_field='title')
    cast = CastSerializer(many=True)

    # def update(self, instance, validated_data, *args, **kwargs):
    #     instance.torrents = validated_data.get('torrents', instance.torrents.set())
    #     instance.save()
    #     return instance

    class Meta:
        model = Movie
        fields = '__all__'
        # fields = ('genres', 'title')
        depth = 2

    # РАБОЧАЯ ВЕРСИЯ
    # TODO Add validation from views.py
    # FIXME "movie with this slug already exists."

    def create(self, validated_data):
        all_cast_names = get_all_cast_names()
        all_char_names = get_all_char_names()
        all_genre_titles = get_all_genre_titles()
        all_movie_slugs = get_all_movie_slugs()

        torrents = validated_data.pop('torrents')
        genres = validated_data.pop('genres')
        cast = validated_data.pop('cast')
        # print(cast)
        movie = Movie.objects.create(**validated_data)
        for tor in torrents:
            Torrents.objects.create(movie=movie, **tor)
        movie.genres.add(*genres)
        movie.save()
        # print(cast)

        iteration_num = 0
        number_of_casts = len(cast)
        # print(cast[iteration_num])
        print('SERIALIZERs')
        # print(cast[0])
        # print(cast[1])
        cast_iteration = 0
        for c in range(number_of_casts):
            for i in cast:
                # print(i['name'])
                # print(i['name'])
                if i['name'] not in all_cast_names:
                    print(i)
                    try:
                    # if i['url_small_image']:
                        new_cast = Cast.objects.create(name=i['name'],
                                                    url_small_image=i['url_small_image'],
                                                    imdb_code=i['imdb_code'])
                        print('NEW CAST \n\n')
                        print(new_cast)
                        new_cast.character_name.create(
                            character_name=i['character_name'],
                            cast=requested_data[num]['cast'][iteration_num]["name"]
                        )
                        movie.cast.add(new_cast)
                        movie.save()
                        all_cast_names = get_all_cast_names()
                        cast_iteration += 1
                    # else:
                    except:
                        new_cast = Cast.objects.create(name=i['name'],
                                                    imdb_code=i['imdb_code'])
                        print(new_cast)
                        new_cast.character_name.create(
                            character_name=i['character_name'],
                            cast=requested_data[num]['cast'][iteration_num]["name"]
                        )
                        movie.cast.add(new_cast)
                        movie.save()
                        all_cast_names = get_all_cast_names()
                        cast_iteration += 1
                else:
                    existing_cast = Cast.objects.get(name=i['name'])
                    movie.cast.add(existing_cast)
                    all_cast_names = get_all_cast_names()
                    # movie.cast.add(i)
                    cast_iteration += 1
                iteration_num += 1
        # movie.save() # Necessary ?
        return movie

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        # representation['torrents'] = TorrentsSerializer(
        # instance.torrents.all(), many=True).data
        # representation['genres'] = MovieSerializer(
        #     instance.genres.all(), many=True).data  # Doesn't needed
        # representation['genres'] = GenreSerializer(
        #     instance.genres.all(), many=True).data
        return representation


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


# class MovieDetailSerializer(serializers.HyperlinkedModelSerializer):
#     # category = serializers.SlugRelatedField(slug_field="name", read_only=True)
#     # cast = CastListSerializer(read_only=True, many=True)
#     qualities = serializers.SlugRelatedField(
#         slug_field="name", read_only=True, many=True)
#     genres = serializers.SlugRelatedField(
#         slug_field="name", read_only=True, many=True)
#     # reviews = ReviewSerializer(many=True)

#     class Meta:
#         model = Movie
#         exclude = ("draft",)
