from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from PIL import Image
from django.urls import reverse

LANGUAGE_CHOICES = (
    ('en', 'English'),
    ('ru', 'Russian'),
    ('de', 'German'),
)


class Director(models.Model):
    """Directors"""
    name = models.CharField(max_length=100)
    born = models.DateField(blank=True, null=True)
    image = models.ImageField(upload_to="directors/")

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse('main:director_movies', kwargs={"slug": self.name})


class Cast(models.Model):
    """Actors"""
    name = models.CharField(max_length=100, blank=True, null=True)
    # born = models.DateField(blank=True, null=True)
    url_small_image = models.URLField(blank=True, null=True)
    imdb_code = models.CharField(max_length=25, blank=True, null=True)

    def __str__(self):
        return self.name

    @property
    def movies(self):
        return self.movie_set.all()

    # def get_absolute_url(self):
    #     return reverse('main:actor_movies', kwargs={"slug": self.name})


class CharacterName(models.Model):
    character_name = models.CharField(max_length=100, blank=True, null=True)
    cast = models.ForeignKey(
        Cast, on_delete=models.CASCADE,
        related_name='character_name',
        blank=True, null=True)

    def __str__(self):
        return self.character_name


class Genre(models.Model):
    title = models.CharField(max_length=55)
    # description = models.TextField()
    # slug = models.SlugField(max_length=125, unique=True)
    # movie = models.ManyToManyField(Movie, related_name='genres')

    def __str__(self):
        return self.title

    # @property
    # def movie(self):
    #     return self.movie.all()


class Movie(models.Model):
    # id = models.CharField(max_length=10)
    imdb_code = models.CharField(max_length=25, null=True, blank=True)
    title = models.CharField(max_length=100, null=True, blank=True)
    slug = models.SlugField(max_length=100, unique=True, null=True, blank=True)
    year = models.IntegerField(null=True, blank=True)
    rating = models.FloatField(null=True, blank=True)
    runtime = models.IntegerField(null=True, blank=True)
    language = models.CharField(max_length=50, blank=True, null=True)

    genres = models.ManyToManyField(Genre)
    cast = models.ManyToManyField(Cast)

    description_full = models.TextField(null=True, blank=True)
    yt_trailer_code = models.CharField(max_length=25, null=True, blank=True)
    background_image = models.URLField(null=True, blank=True)
    background_image_original = models.URLField(null=True, blank=True)
    small_cover_image = models.URLField(null=True, blank=True)
    medium_cover_image = models.URLField(null=True, blank=True)
    large_cover_image = models.URLField(null=True, blank=True)
    medium_screenshot_image1 = models.URLField(null=True, blank=True)
    medium_screenshot_image2 = models.URLField(null=True, blank=True)
    medium_screenshot_image3 = models.URLField(null=True, blank=True)
    large_screenshot_image1 = models.URLField(null=True, blank=True)
    large_screenshot_image2 = models.URLField(null=True, blank=True)
    large_screenshot_image3 = models.URLField(null=True, blank=True)

    # published = models.DateTimeField(default=timezone.now)

    # directors = models.ManyToManyField(Director, related_name="film_director")
    # files = models.ForeignKey(Quality, on_delete=models.CASCADE, blank=True, null=True)

    # class Meta:
    #     ordering = ('-published',)

    def __str__(self):
        return self.title

    def get_review(self):
        return self.reviews_set.filter(parent__isnull=True)

    def get_absolute_url(self):
        return reverse('main:movie_detail',
                       kwargs={'slug': self.slug})

    @property
    def torrents(self):
        return self.torrents_set.all()


    # @property
    # def genres(self):
    #     return self.genres.all()

    # # Resizing the image
    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)

    #     img = Image.open(self.image.path)

    #     if img.height > 300 and img.width > 300:
    #         output_size = (300, 300)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)


class Torrents(models.Model):
    """
    Torrent files
    """

    url = models.URLField(null=True, blank=True)
    quality = models.CharField(max_length=15, null=True, blank=True)
    quality_type = models.CharField(max_length=15, null=True, blank=True)
    seeds = models.CharField(max_length=15, null=True, blank=True)
    peers = models.CharField(max_length=15, null=True, blank=True)
    size = models.CharField(max_length=15, null=True, blank=True)

    movie = models.ForeignKey(
        Movie, on_delete=models.CASCADE, null=True, blank=True, related_name='torrents')

    class Meta:
        verbose_name_plural = 'Torrents'


class Subtitles(models.Model):
    language = models.CharField(
        max_length=55, choices=LANGUAGE_CHOICES, default='en')
    sub_file = models.FileField(upload_to='subtitles', null=True, blank=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return self.language


# class Rating(models.Model):
#     stars = models.FloatField()  # FROM IMDb
#     rates = models.CharField(max_length=5)  # Number of rates
#     movie = models.ManyToManyField(Movie)
#     # movie = models.OneToOneField(Movie, on_delete=models.CASCADE)


class Reviews(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=100)
    text = models.TextField(max_length=5000)
    parent = models.ForeignKey(
        'self', on_delete=models.SET_NULL, blank=True, null=True
    )
    # avatar = models.ImageField(default='images/default-user.jpg' , blank=True, null=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.movie}"


class MovieShots(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="movie_shots/")
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
