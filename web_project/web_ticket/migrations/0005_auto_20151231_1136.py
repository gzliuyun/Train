# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-31 03:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_ticket', '0004_auto_20151231_1107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userorders',
            name='userid',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='users',
            name='userid',
            field=models.CharField(max_length=30),
        ),
    ]
