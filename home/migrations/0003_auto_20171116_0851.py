# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-16 02:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20171116_0741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='height_field',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='width_field',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]