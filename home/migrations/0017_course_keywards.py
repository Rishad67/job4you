# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-18 17:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_auto_20171118_2158'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='keywards',
            field=models.TextField(help_text='Enter some keywards of course', max_length=200, null=True),
        ),
    ]
