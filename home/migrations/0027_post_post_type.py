# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-17 11:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0026_auto_20180117_0856'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_type',
            field=models.CharField(blank=True, choices=[('p', 'problems and solutions'), ('i', 'instructors stories'), ('s', 'students success'), ('c', 'career guideline')], max_length=1),
        ),
    ]
