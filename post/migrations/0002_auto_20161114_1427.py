# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-14 14:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]