from rest_framework import serializers
from main.models import Movie, Genre, Torrents, Cast


class TorrentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Torrents
        # queryset = Torrents.objects.all()
        fields = '__all__'
        # depth = 1
    
class CastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cast
        # queryset = Torrents.objects.all()
        fields = '__all__'
        # depth = 1


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    torrents = TorrentsSerializer(many=True)
    genres = serializers.SlugRelatedField(
        queryset=Genre.objects.all(), many=True, slug_field='title')
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
        print(validated_data)
        cast = validated_data.pop('cast')
        movie = Movie.objects.create(**validated_data)
        for tor in torrents:
            Torrents.objects.create(movie=movie, **tor)
        movie.genres.add(*genres)
        print(cast)
        movie.cast.add(*cast)
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
