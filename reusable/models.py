from django.db import models


class Merch(models.Model):
    """
    Merch related to movies, series.
    """
    title = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    merch_url = models.URLField(null=True, blank=True)
    image = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.title


class Collection(models.Model):
    """
    Collections of similar movies, from one company, one series, depends on 
    the mood and so on.
    """
    title = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    medium_image = models.URLField(null=True, blank=True)
    large_image = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.title
