# Generated by Django 3.0.7 on 2020-07-02 15:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0036_auto_20200702_1822'),
    ]

    operations = [
        migrations.AlterField(
            model_name='torrents',
            name='movie',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='torrents', to='main.Movie'),
        ),
    ]