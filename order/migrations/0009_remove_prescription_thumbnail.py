# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-10 09:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0008_auto_20160810_0835'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prescription',
            name='thumbnail',
        ),
    ]
