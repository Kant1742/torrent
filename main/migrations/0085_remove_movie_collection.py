# Generated by Django 3.0.7 on 2020-07-31 08:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0084_auto_20200731_1156'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='collection',
        ),
    ]
