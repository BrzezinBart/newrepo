# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-13 09:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ankieta', '0003_auto_20170313_0942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ankieta_model',
            name='data_z',
            field=models.DateField(validators='none'),
        ),
    ]
