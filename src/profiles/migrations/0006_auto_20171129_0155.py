# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-29 01:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_profile_job'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='location',
            field=models.CharField(blank=True, default='my location default', max_length=120, null=True),
        ),
    ]
