# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-16 02:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20171116_0853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='height_field',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='profile',
            name='width_field',
            field=models.IntegerField(default=0),
        ),
    ]