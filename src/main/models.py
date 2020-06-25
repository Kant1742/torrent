from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from PIL import Image
from django.urls import reverse


class Director(models.Model):
    """Directors"""
    name = models.CharField(max_length=100)
    born = models.DateField(blank=True, null=True)
    image = models.ImageField(upload_to="directors/")

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse('main:director_movies', kwargs={"slug": self.name})


class Actor(models.Model):
    """Actors"""
    name = models.CharField(max_length=100)
    born = models.DateField(blank=True, null=True)
    image = models.ImageField(upload_to="actors/")

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse('main:actor_movies', kwargs={"slug": self.name})


class Genre(models.Model):
    title = models.CharField(max_length=55)
    description = models.TextField()
    slug = models.SlugField(max_length=125, unique=True)

    def __str__(self):
        return self.title


class Movie(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    year = models.IntegerField()
    description = models.TextField()

    image = models.ImageField(
        upload_to='movie-images', null=True, blank=True
    )
    published = models.DateTimeField(default=timezone.now)

    # quality = models.ManyToManyField(Quality)

    actors = models.ManyToManyField(Actor, related_name="film_actor")
    directors = models.ManyToManyField(Director, related_name="film_director")
    genres = models.ManyToManyField(Genre)
    # files = models.ForeignKey(Quality, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        ordering = ('-published',)

    def __str__(self):
        return self.title

    def get_review(self):
        return self.reviews_set.filter(parent__isnull=True)

    def get_absolute_url(self):
        return reverse('main:movie_detail',
                       kwargs={'slug': self.slug})

    # Resizing the image
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 and img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


class Quality(models.Model):
    """
    The quality of movies
    """
    # STATUS_CHOICES = (
    #     ('360', '360p'),
    #     ('480', '480p'),
    #     ('720', 'HD 720p'),
    #     ('1080', 'FullHD 1080p'),
    # )
    # quality = models.CharField(max_length=4, null=True, blank=True)
    # file = models.FileField(upload_to='files', null=True, blank=True)
    quality_360 = models.FileField(
        upload_to='files', null=True, blank=True)
    quality_480 = models.FileField(
        upload_to='files', null=True, blank=True)
    quality_720 = models.FileField(
        upload_to='files', null=True, blank=True)
    quality_1080 = models.FileField(
        upload_to='files', null=True, blank=True)

    movie = models.OneToOneField(
        Movie, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Qualities'

    # def __str__(self):
    #     try:
    #         return self.movie
    #     except:
    #         pass


LANGUAGE_CHOICES = (
    ('en', 'English'),
    ('ru', 'Russian'),
    ('de', 'German'),
)


class Subtitles(models.Model):
    language = models.CharField(
        max_length=55, choices=LANGUAGE_CHOICES, default='en')
    sub_file = models.FileField(upload_to='subtitles', null=True, blank=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return self.language


class Rating(models.Model):
    stars = models.FloatField()  # FROM IMDb
    rates = models.CharField(max_length=5)  # Number of rates
    # movie = models.ManyToManyField(Movie)
    movie = models.OneToOneField(Movie, on_delete=models.CASCADE)


class Reviews(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=100)
    text = models.TextField(max_length=5000)
    parent = models.ForeignKey(
        'self', on_delete=models.SET_NULL, blank=True, null=True
    )
    # avatar = models.ImageField(default='default-user.jpg' , blank=True, null=True)
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
