# Generated by Django 3.0.7 on 2020-07-23 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0071_auto_20200723_1929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='language',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]