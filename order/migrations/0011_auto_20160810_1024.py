# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-10 10:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0010_auto_20160810_0940'),
    ]

    operations = [
        migrations.AddField(
            model_name='prescription',
            name='thumbnail',
            field=models.ImageField(blank=True, height_field='height', upload_to='uploads/prescription', width_field='width'),
        ),
        migrations.AlterField(
            model_name='prescription',
            name='image',
            field=models.ImageField(blank=True, height_field='height', upload_to='uploads/prescription', width_field='width'),
        ),
    ]
