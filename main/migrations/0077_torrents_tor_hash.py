# Generated by Django 3.0.7 on 2020-07-30 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0076_auto_20200728_2113'),
    ]

    operations = [
        migrations.AddField(
            model_name='torrents',
            name='tor_hash',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]