# Generated by Django 3.0.7 on 2020-07-31 09:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reusable', '0011_remove_collection_collection_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='merch',
            name='collection_type',
        ),
    ]