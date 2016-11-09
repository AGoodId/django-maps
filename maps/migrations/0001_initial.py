# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GMap',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('address', models.CharField(unique=True, max_length=255, verbose_name='Address')),
                ('formatted_address', models.CharField(max_length=255, verbose_name='Formatted address', blank=True)),
                ('latitude', models.FloatField(verbose_name='Latitude', blank=True)),
                ('longitude', models.FloatField(verbose_name='Longitude', blank=True)),
                ('geocode_error', models.BooleanField(default=False, verbose_name='Geocode error')),
                ('geocode_error_message', models.CharField(max_length=255, verbose_name='Error message', blank=True)),
            ],
            options={
                'verbose_name': 'Google Map Address',
                'verbose_name_plural': 'Google Map Addresses',
            },
        ),
    ]
