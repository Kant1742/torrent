from django.db import models
from django.utils import timezone
from django.urls import reverse

def image_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/<collection_name>/<filename>
    return f'{instance}/{filename}'


class ReusableFields(models.Model):
    """
    Most common fields.
    """
    title = models.CharField(max_length=100, null=True, blank=True)
    slug = models.SlugField(max_length=100, unique=True, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        abstract = True


class Collection(ReusableFields):
    """
    Collections of similar movies, from one company, one series, depends on 
    the mood and so on.
    """
    published = models.DateTimeField(
        default=timezone.now, blank=True, null=True)

    class Meta:
        ordering = ('-published',)

    def get_absolute_url(self):
        return reverse('reusable:collection_items',
                       kwargs={'slug': self.slug})


class Company(ReusableFields):
    """
    Creator movies
    """
    collections = models.ForeignKey(
        Collection, on_delete=models.DO_NOTHING, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Companies'


class Merch(ReusableFields):
    """
    Merch related to movies, series.
    """
    merch_url = models.URLField(null=True, blank=True)
    published = models.DateTimeField(
        default=timezone.now, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Merch'

    def __str__(self):
        return self.title
