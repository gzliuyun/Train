# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-29 08:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_ticket', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordernum', models.CharField(max_length=50)),
                ('orderdate', models.DateField()),
                ('trainnumber', models.CharField(max_length=20)),
                ('startdate', models.DateField()),
                ('seattype', models.CharField(max_length=20)),
                ('seatnumber', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Ticketcounts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trainnumber', models.CharField(max_length=20)),
                ('startdate', models.DateField()),
                ('businessseat', models.IntegerField(blank=True)),
                ('businessseattotal', models.IntegerField(blank=True)),
                ('principalseat', models.IntegerField(blank=True)),
                ('principalseattotal', models.IntegerField(blank=True)),
                ('firstclassseat', models.IntegerField(blank=True)),
                ('firstclassseattotal', models.IntegerField(blank=True)),
                ('secondclassseat', models.IntegerField(blank=True)),
                ('secondclassseattotal', models.IntegerField(blank=True)),
                ('advancedsoftsleeper', models.IntegerField(blank=True)),
                ('advancedsoftsleepertotal', models.IntegerField(blank=True)),
                ('softsleeper', models.IntegerField(blank=True)),
                ('softsleepertotal', models.IntegerField(blank=True)),
                ('hardsleeper', models.IntegerField(blank=True)),
                ('hardsleepertotal', models.IntegerField(blank=True)),
                ('softseat', models.IntegerField(blank=True)),
                ('softseattotal', models.IntegerField(blank=True)),
                ('hardseat', models.IntegerField(blank=True)),
                ('hardseattotal', models.IntegerField(blank=True)),
                ('noseat', models.IntegerField(blank=True)),
                ('noseattotal', models.IntegerField(blank=True)),
                ('others', models.IntegerField(blank=True)),
                ('otherstotal', models.IntegerField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ticketinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trainnumber', models.CharField(max_length=20)),
                ('startstation', models.CharField(max_length=20)),
                ('destination', models.CharField(max_length=20)),
                ('starttime', models.TimeField()),
                ('arrivetime', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Userorders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.CharField(max_length=20)),
                ('ordernum', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('userid', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=20)),
                ('cardid', models.CharField(max_length=20)),
                ('phonenumber', models.CharField(max_length=20)),
                ('email', models.EmailField(blank=True, max_length=254)),
            ],
        ),
        migrations.DeleteModel(
            name='Ticket',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
