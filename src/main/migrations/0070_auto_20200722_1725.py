# Generated by Django 3.0.7 on 2020-07-22 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0069_auto_20200722_1654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='download_count',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='like_count',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
