# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-23 05:49
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendanceMgnt', '0008_auto_20170515_0613'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='date',
            field=models.DateField(default=datetime.date.today, verbose_name='Date'),
        ),
    ]