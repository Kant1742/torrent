# Generated by Django 3.0.7 on 2020-06-23 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20200623_1051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='torrent',
            name='year',
            field=models.IntegerField(),
        ),
    ]
