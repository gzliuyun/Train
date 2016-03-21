# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-02 11:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_ticket', '0007_auto_20160102_1346'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Ticketback',
            new_name='Ticketbacks',
        ),
        migrations.DeleteModel(
            name='Userorders',
        ),
        migrations.RenameField(
            model_name='orders',
            old_name='ordernum',
            new_name='ordernumber',
        ),
        migrations.AddField(
            model_name='orders',
            name='userid',
            field=models.CharField(default=0, max_length=30),
            preserve_default=False,
        ),
    ]
