# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-05 06:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='avatar',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]