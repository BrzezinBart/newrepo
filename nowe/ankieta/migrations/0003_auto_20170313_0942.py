# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-13 09:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ankieta', '0002_auto_20170313_0926'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ankieta_model',
            old_name='data_zakonczenia',
            new_name='data_z',
        ),
    ]