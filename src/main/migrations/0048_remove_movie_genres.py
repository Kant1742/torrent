# Generated by Django 3.0.7 on 2020-07-07 15:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0047_auto_20200705_1511'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='genres',
        ),
    ]
