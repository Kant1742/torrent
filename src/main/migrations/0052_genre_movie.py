# Generated by Django 3.0.7 on 2020-07-07 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0051_remove_genre_movie'),
    ]

    operations = [
        migrations.AddField(
            model_name='genre',
            name='movie',
            field=models.ManyToManyField(related_name='genres', to='main.Movie'),
        ),
    ]
