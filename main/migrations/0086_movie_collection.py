# Generated by Django 3.0.7 on 2020-07-31 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reusable', '0012_remove_merch_collection_type'),
        ('main', '0085_remove_movie_collection'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='collection',
            field=models.ManyToManyField(blank=True, to='reusable.Collection'),
        ),
    ]