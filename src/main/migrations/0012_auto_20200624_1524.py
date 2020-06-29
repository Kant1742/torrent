# Generated by Django 3.0.7 on 2020-06-24 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20200624_1040'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='quality',
            options={'verbose_name_plural': 'Qualities'},
        ),
        migrations.RemoveField(
            model_name='movie',
            name='file',
        ),
        migrations.RemoveField(
            model_name='subtitles',
            name='file',
        ),
        migrations.AddField(
            model_name='subtitles',
            name='sub_file',
            field=models.FileField(blank=True, null=True, upload_to='subtitles'),
        ),
        migrations.AlterField(
            model_name='quality',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='files'),
        ),
        migrations.DeleteModel(
            name='File',
        ),
    ]