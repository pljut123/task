# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-16 12:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginsys', '0005_auto_20161116_1219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='image/', verbose_name='image'),
        ),
    ]