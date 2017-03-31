# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-22 09:29
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ankieta', '0013_auto_20170322_0916'),
    ]

    operations = [
        migrations.AddField(
            model_name='ankietamodel',
            name='autor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]