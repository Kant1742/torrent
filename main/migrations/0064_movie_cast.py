# Generated by Django 3.0.7 on 2020-07-17 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0063_remove_movie_cast'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='cast',
            field=models.ManyToManyField(to='main.Cast'),
        ),
    ]
