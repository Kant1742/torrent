# Generated by Django 3.0.7 on 2020-12-02 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reusable', '0024_auto_20200810_1217'),
        ('main', '0088_auto_20200804_1801'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='collection',
            field=models.ManyToManyField(blank=True, related_name='collection_movies', to='reusable.Collection'),
        ),
    ]
