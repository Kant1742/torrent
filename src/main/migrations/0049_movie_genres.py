# Generated by Django 3.0.7 on 2020-07-07 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0048_remove_movie_genres'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='genres',
            field=models.ManyToManyField(related_name='genres', to='main.Genre'),
        ),
    ]
