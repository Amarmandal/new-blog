# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-14 13:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_post_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='description',
        ),
        migrations.AddField(
            model_name='post',
            name='shortt',
            field=models.TextField(blank=True),
        ),
    ]
