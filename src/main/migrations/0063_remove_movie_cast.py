# Generated by Django 3.0.7 on 2020-07-17 11:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0062_auto_20200711_2014'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='cast',
        ),
    ]
