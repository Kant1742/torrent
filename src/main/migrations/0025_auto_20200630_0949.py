# Generated by Django 3.0.7 on 2020-06-30 06:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0024_auto_20200630_0941'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='description',
            new_name='description_full',
        ),
    ]