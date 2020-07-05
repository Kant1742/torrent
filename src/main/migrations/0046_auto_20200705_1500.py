# Generated by Django 3.0.7 on 2020-07-05 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0045_movie_genres'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='genres',
        ),
        migrations.AddField(
            model_name='genre',
            name='movie',
            field=models.ManyToManyField(to='main.Movie'),
        ),
    ]