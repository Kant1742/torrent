# Generated by Django 3.0.7 on 2020-08-10 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reusable', '0023_auto_20200804_1937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='company',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='merch',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
