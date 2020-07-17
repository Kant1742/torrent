from .models import Cast, Genre, Movie, CharacterName


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
