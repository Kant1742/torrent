from django.db import models


class Merch(models.Model):
    """
    Merch related to movies, series.
    """
    title = models.CharField(max_length=100, null=True, blank=True)
    slug = models.SlugField(max_length=100, unique=True, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    merch_url = models.URLField(null=True, blank=True)
    image = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.title

    # # Resizing the image
    def save(self, *args, **kwargs):
        try:
            super().save(*args, **kwargs)

            img = Image.open(self.image.path)

            if img.height > 225 and img.width > 150:
                output_size = (225, 150)
                img.thumbnail(output_size)
                img.save(self.image.path)
        except:
            print('We recommend you add an image')


class Collection(models.Model):
    """
    Collections of similar movies, from one company, one series, depends on 
    the mood and so on.
    """
    title = models.CharField(max_length=100, null=True, blank=True)
    slug = models.SlugField(max_length=100, unique=True, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        try:
            super().save(*args, **kwargs)

            img = Image.open(self.image.path)

            if img.height > 225 and img.width > 150:
                output_size = (225, 150)
                img.thumbnail(output_size)
                img.save(self.image.path)
        except:
            print('We recommend you add an image')
