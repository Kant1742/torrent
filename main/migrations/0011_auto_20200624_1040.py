# Generated by Django 3.0.7 on 2020-06-24 07:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20200623_1836'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file',
            name='movie',
        ),
        migrations.AddField(
            model_name='movie',
            name='file',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.File'),
        ),
        migrations.AddField(
            model_name='quality',
            name='file',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.File'),
        ),
        migrations.AlterField(
            model_name='actor',
            name='born',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='director',
            name='born',
            field=models.DateField(blank=True, null=True),
        ),
    ]