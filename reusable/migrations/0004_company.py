# Generated by Django 3.0.7 on 2020-07-30 17:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reusable', '0003_auto_20200728_2132'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('slug', models.SlugField(blank=True, max_length=100, null=True, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.URLField(blank=True, null=True)),
                ('collections', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='reusable.Collection')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
