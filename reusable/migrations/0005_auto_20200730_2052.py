# Generated by Django 3.0.7 on 2020-07-30 17:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reusable', '0004_company'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='company',
            options={'verbose_name_plural': 'Companies'},
        ),
        migrations.AlterModelOptions(
            name='merch',
            options={'verbose_name_plural': 'Merch'},
        ),
    ]
