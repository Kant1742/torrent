# Generated by Django 3.0.7 on 2020-06-25 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_auto_20200625_1412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='stars',
            field=models.FloatField(),
        ),
    ]
