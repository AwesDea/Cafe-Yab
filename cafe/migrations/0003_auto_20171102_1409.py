# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-02 14:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafe', '0002_cafe_verified'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cafe',
            name='description',
            field=models.TextField(max_length=1000),
        ),
    ]
