# Generated by Django 3.0.7 on 2020-07-02 11:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0031_auto_20200702_1401'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quality',
            name='movie',
        ),
        migrations.AddField(
            model_name='movie',
            name='qualities',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Quality'),
        ),
    ]