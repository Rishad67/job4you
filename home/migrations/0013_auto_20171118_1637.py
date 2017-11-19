# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-18 10:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_course_lesson'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='launch_date',
        ),
        migrations.AddField(
            model_name='course',
            name='active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='course',
            name='last_update',
            field=models.DateField(null=True),
        ),
    ]