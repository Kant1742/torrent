# Generated by Django 3.0.7 on 2020-07-17 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0065_remove_movie_cast'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='cast',
            field=models.ManyToManyField(to='main.Cast'),
        ),
    ]
