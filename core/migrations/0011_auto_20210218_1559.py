# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2021-02-18 15:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20210218_1447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animais',
            name='idade',
            field=models.CharField(blank=True, max_length=2, null=True),
        ),
    ]