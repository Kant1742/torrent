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
        # queryset = Torrents.objects.all()
        fields = '__all__'
        # depth = 1


class CharacterNameSerializer(serializers.ModelSerializer):
    # cast = serializers.SlugRelatedField(
    #     queryset=CharacterName.objects.all(), slug_field='cast__name')
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
    # character_names = serializers.SlugRelatedField(
    #     queryset=CharacterName.objects.all(), slug_field='characters_name')
    # character_name = CharacterName.objects.filter()
    # movie = serializers.SlugRelatedField(queryset=Movie.objects.all(), slug_field='title')
    # character_name = CharacterNameSerializer()
    # character_name = serializers.StringRelatedField(many=True)

    class Meta:
        model = Cast
        # queryset = Torrents.objects.all()
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
    # cast = serializers.SlugRelatedField(
    #     queryset=Cast.objects.filter(), many=True, slug_field='name')
    cast = CastSerializer(many=True)
    # genres = GenreSerializer(many=True)

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
    def create(self, validated_data):
        torrents = validated_data.pop('torrents')
        genres = validated_data.pop('genres')
        cast = validated_data.pop('cast')
        movie = Movie.objects.create(**validated_data)
        for tor in torrents:
            Torrents.objects.create(movie=movie, **tor)
        movie.genres.add(*genres)
        movie.save()
        for i in cast:
            print(i['name'])
            print('\n\n')
            print(cast)
            new_cast = Cast.objects.create(name=i['name'],
                                           url_small_image=i['url_small_image'],
                                           imdb_code=i['imdb_code']
                                           )
            movie.cast.add(new_cast)
        movie.save()
        # print(cast[0]['name'])
        """ По сути здесь я нихуя не менял, кроме того, что вместо *cast
        добавляют его ID.
        Решения: получение id от cast 
                 SlugRelatedField (или PrimaryKeyRelatedField)
                 заебенить это добавление во вьюхе, там и получать через слаг"""
        # movie.cast.add(cast[0]['name'])
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
