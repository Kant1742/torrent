# Generated by Django 3.0.7 on 2020-07-08 16:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0053_auto_20200707_1937'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='genres',
        ),
    ]