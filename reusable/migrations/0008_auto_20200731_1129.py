# Generated by Django 3.0.7 on 2020-07-31 08:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reusable', '0007_auto_20200730_2200'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='collection',
            name='collection_type',
        ),
        migrations.RemoveField(
            model_name='merch',
            name='collection_type',
        ),
    ]
