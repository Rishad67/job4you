# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-18 15:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_auto_20171118_1720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='rating',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
    ]