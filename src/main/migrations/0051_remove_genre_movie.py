# Generated by Django 3.0.7 on 2020-07-07 16:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0050_auto_20200707_1902'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='genre',
            name='movie',
        ),
    ]
