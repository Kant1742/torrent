# Generated by Django 3.0.7 on 2020-07-05 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0046_auto_20200705_1500'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='genre',
            name='movie',
        ),
        migrations.AddField(
            model_name='movie',
            name='genres',
            field=models.ManyToManyField(related_name='genres', to='main.Genre'),
        ),
    ]
