# Generated by Django 3.0.7 on 2020-07-23 16:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0070_auto_20200722_1725'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='movie',
            options={'ordering': ('-published',)},
        ),
    ]