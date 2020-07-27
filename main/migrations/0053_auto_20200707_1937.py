# Generated by Django 3.0.7 on 2020-07-07 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0052_genre_movie'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='genre',
            name='movie',
        ),
        migrations.AddField(
            model_name='movie',
            name='genres',
            field=models.ManyToManyField(to='main.Genre'),
        ),
    ]