# Generated by Django 3.0.7 on 2020-07-11 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0058_auto_20200711_0813'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cast',
            name='character_name',
        ),
        migrations.CreateModel(
            name='CharacterName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('character_name', models.CharField(blank=True, max_length=100, null=True)),
                ('cast', models.ManyToManyField(to='main.Cast')),
            ],
        ),
    ]