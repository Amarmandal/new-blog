# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-15 13:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0005_auto_20171214_1852'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='short',
        ),
    ]