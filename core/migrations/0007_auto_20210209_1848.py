# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2021-02-09 18:48
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20210209_1845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoas',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
