# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-13 18:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0021_auto_20180114_0025'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='catagory',
            field=models.CharField(blank=True, choices=[('bu', 'Business'), ('it', 'IT & Software'), ('pt', 'Photography'), ('hf', 'Health & fitness'), ('an', 'Android'), ('wd', 'Web Design'), ('ai', 'Artificial Intelligence'), ('gm', 'Gameing'), ('rb', 'Robotics'), ('ds', 'Design'), ('mc', 'Machine Learning'), ('tc', 'Teaching'), ('pl', 'Programming Language')], max_length=2),
        ),
    ]
