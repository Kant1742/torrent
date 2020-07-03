# Generated by Django 3.0.7 on 2020-07-02 10:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0028_auto_20200630_1017'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quality',
            name='movie',
        ),
        migrations.AddField(
            model_name='movie',
            name='quality',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Quality'),
        ),
    ]