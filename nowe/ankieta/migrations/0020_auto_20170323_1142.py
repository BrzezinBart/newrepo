# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-23 11:42
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ankieta', '0019_auto_20170323_1134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ankietamodel',
            name='data_w',
            field=models.DateTimeField(default=datetime.datetime(2017, 3, 30, 11, 42, 30, 671875)),
        ),
    ]
