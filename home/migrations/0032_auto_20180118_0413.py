# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-17 22:13
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0031_auto_20180118_0312'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='follow',
            name='instructor',
        ),
        migrations.RemoveField(
            model_name='follow',
            name='student',
        ),
        migrations.AddField(
            model_name='profile',
            name='follower',
            field=models.ManyToManyField(related_name='follower', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Follow',
        ),
    ]
