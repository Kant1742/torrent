# Generated by Django 3.0.7 on 2020-07-31 14:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reusable', '0013_collection_short_description'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='collection',
            options={'ordering': ('-published',)},
        ),
    ]