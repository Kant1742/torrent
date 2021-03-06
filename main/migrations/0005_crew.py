# Generated by Django 3.0.7 on 2020-06-23 08:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20200623_1057'),
    ]

    operations = [
        migrations.CreateModel(
            name='Crew',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('director', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='director', to='main.Torrent')),
                ('stars', models.ManyToManyField(related_name='stars', to='main.Torrent')),
            ],
        ),
    ]
