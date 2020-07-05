from rest_framework import serializers
from main.models import Movie, Genre, Torrents


class TorrentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Torrents
        # queryset = Torrents.objects.all()
        fields = '__all__'
        # depth = 1


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    torrents = TorrentsSerializer(many=True)
    # genres = serializers.SlugRelatedField(queryset=Genre.objects.all(), many=True, slug_field='title')
    genres = GenreSerializer(many=True)

    # def update(self, instance, validated_data, *args, **kwargs):
    #     instance.torrents = validated_data.get('torrents', instance.torrents.set())
    #     instance.save()
    #     return instance

    class Meta:
        model = Movie
        fields = '__all__'
        depth = 2

    # РАБОЧАЯ ВЕРСИЯ, НО БЕЗ ДОБАВЛЕНИЯ ЖАНРОВ
    def create(self, validated_data):
        torrents = validated_data.pop('torrents')
        movie = Movie.objects.create(**validated_data)
        for tor in torrents:
            Torrents.objects.create(movie=movie, **tor)
        return movie


    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['torrents'] = TorrentsSerializer(
            instance.torrents.all(), many=True).data
        return representation


    # def create(self, validated_data, *args, **kwargs):
    #     torrents = validated_data.pop('torrents')
    #     movie = Movie.objects.create(**validated_data)
    #     for tor in torrents:
    #         Torrents.objects.create(movie=movie, **tor)
    #     return movie

    # def update(self, instance, validated_data):
    #     torrents = validated_data.pop('torrents')
    #     instance.title = validated_data.get('title', instance.title)
    #     instance.save()
    #     keep_torrents = []
    #     existing_torrents = [t.url for t in instance.torrents]

    # def create(self, validated_data):
    #     torrents_data = validated_data.pop('torrents')
    #     genres_data = validated_data.pop('genres')
    #     torrents = Torrents.objects.create(**validated_data)
    #     genres = Genre.objects.create(**validated_data)
    #     movie = Movie.objects.create(torrents=torrents, genres=genres, **validated_data)
    #     return movie

# def to_representation(self, instance):
#     response = super().to_representation(instance)
#     response['torrents'] = TorrentsSerializer(instance.child).data
#     return response




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
