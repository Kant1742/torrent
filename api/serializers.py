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
    cast = CastSerializer(many=True, required=False)
    iteration_num = 0

    # def update(self, instance, validated_data, *args, **kwargs):
    #     instance.torrents = validated_data.get('torrents', instance.torrents.set())
    #     instance.save()
    #     return instance

    class Meta:
        model = Movie
        fields = '__all__'
        # fields = ('genres', 'title')
        depth = 2

    def create(self, validated_data):
        all_cast_names = get_all_cast_names()
        all_char_names = get_all_char_names()
        all_genre_titles = get_all_genre_titles()
        all_movie_slugs = get_all_movie_slugs()

        torrents = validated_data.pop('torrents')
        genres = validated_data.pop('genres')
        # FIXME 'cast' this field is required
        try:
            cast = validated_data.pop('cast')
        except:
            print('Serializers no cast')
        movie = Movie.objects.create(**validated_data)
        for tor in torrents:
            Torrents.objects.create(movie=movie, **tor)
        movie.genres.add(*genres)
        movie.save()

        # An example
        # profile_data = validated_data.pop('profile', {})
        # for (key, value) in profile_data.items():
        #     setattr(instance.profile, key, value)

        try:
            number_of_casts = len(cast)
            for c in range(number_of_casts):
                for i in cast:
                    if i['name'] not in all_cast_names:
                        new_cast = Cast.objects.create(name=i['name'],
                                                    url_small_image=i['url_small_image'],
                                                    imdb_code=i['imdb_code'])
                        movie.cast.add(new_cast)
                        movie.save()
                        all_cast_names = get_all_cast_names()
                    else:
                        existing_cast = Cast.objects.get(name=i['name'])
                        movie.cast.add(existing_cast)
                        all_cast_names = get_all_cast_names()
                    print('In for cast')
        except:
            pass
        print(f'serializers --- {self.iteration_num}')
        self.iteration_num += 1
        return movie


    ''' 
    # From django-real-world-examples


    def update(self, instance, validated_data):
        """Performs an update on a User."""

        # Passwords should not be handled with `setattr`, unlike other fields.
        # This is because Django provides a function that handles hashing and
        # salting passwords, which is important for security. What that means
        # here is that we need to remove the password field from the
        # `validated_data` dictionary before iterating over it.
        password = validated_data.pop('password', None)

        # Like passwords, we have to handle profiles separately. To do that,
        # we remove the profile data from the `validated_data` dictionary.
        profile_data = validated_data.pop('profile', {})

        for (key, value) in validated_data.items():
            # For the keys remaining in `validated_data`, we will set them on
            # the current `User` instance one at a time.
            setattr(instance, key, value)

        if password is not None:
            # `.set_password()` is the method mentioned above. It handles all
            # of the security stuff that we shouldn't be concerned with.
            instance.set_password(password)

        # Finally, after everything has been updated, we must explicitly save
        # the model. It's worth pointing out that `.set_password()` does not
        # save the model.
        instance.save()

        for (key, value) in profile_data.items():
            # We're doing the same thing as above, but this time we're making
            # changes to the Profile model.
            setattr(instance.profile, key, value)
            
        # Save the profile just like we saved the user.
        instance.profile.save()

        return instance
    '''

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        return representation


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'
