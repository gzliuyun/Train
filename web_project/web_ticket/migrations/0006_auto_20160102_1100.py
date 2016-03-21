# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-02 03:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_ticket', '0005_auto_20151231_1136'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ticketinfo',
            old_name='price',
            new_name='advancedsoftseatprice',
        ),
        migrations.RemoveField(
            model_name='ticketcounts',
            name='advancedsoftsleepertotal',
        ),
        migrations.RemoveField(
            model_name='ticketcounts',
            name='businessseattotal',
        ),
        migrations.RemoveField(
            model_name='ticketcounts',
            name='firstclassseattotal',
        ),
        migrations.RemoveField(
            model_name='ticketcounts',
            name='hardseattotal',
        ),
        migrations.RemoveField(
            model_name='ticketcounts',
            name='hardsleepertotal',
        ),
        migrations.RemoveField(
            model_name='ticketcounts',
            name='noseattotal',
        ),
        migrations.RemoveField(
            model_name='ticketcounts',
            name='otherstotal',
        ),
        migrations.RemoveField(
            model_name='ticketcounts',
            name='principalseattotal',
        ),
        migrations.RemoveField(
            model_name='ticketcounts',
            name='secondclassseattotal',
        ),
        migrations.RemoveField(
            model_name='ticketcounts',
            name='softseattotal',
        ),
        migrations.RemoveField(
            model_name='ticketcounts',
            name='softsleepertotal',
        ),
        migrations.AddField(
            model_name='ticketinfo',
            name='advancedsoftseattotal',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='ticketinfo',
            name='businessseatprice',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='ticketinfo',
            name='businessseattotal',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='ticketinfo',
            name='firstclassseatprice',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='ticketinfo',
            name='firstclassseattotal',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='ticketinfo',
            name='hardseatprice',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='ticketinfo',
            name='hardseattotal',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='ticketinfo',
            name='hardsleeperprice',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='ticketinfo',
            name='hardsleepertotal',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='ticketinfo',
            name='noseatprice',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='ticketinfo',
            name='noseattotal',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='ticketinfo',
            name='othersprice',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='ticketinfo',
            name='otherstotal',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='ticketinfo',
            name='principalseatprice',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='ticketinfo',
            name='principalseattotal',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='ticketinfo',
            name='secondclassseatprice',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='ticketinfo',
            name='secondclassseattotal',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='ticketinfo',
            name='softseatprice',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='ticketinfo',
            name='softseattotal',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='ticketinfo',
            name='softsleeperprice',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='ticketinfo',
            name='softsleeperttotal',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='ticketcounts',
            name='advancedsoftsleeper',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='ticketcounts',
            name='businessseat',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='ticketcounts',
            name='firstclassseat',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='ticketcounts',
            name='hardseat',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='ticketcounts',
            name='hardsleeper',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='ticketcounts',
            name='noseat',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='ticketcounts',
            name='others',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='ticketcounts',
            name='principalseat',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='ticketcounts',
            name='secondclassseat',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='ticketcounts',
            name='softseat',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='ticketcounts',
            name='softsleeper',
            field=models.IntegerField(default=0),
        ),
    ]
