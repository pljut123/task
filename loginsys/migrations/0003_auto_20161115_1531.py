# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-15 15:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginsys', '0002_auto_20161115_1530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='image/', verbose_name='image'),
        ),
    ]
