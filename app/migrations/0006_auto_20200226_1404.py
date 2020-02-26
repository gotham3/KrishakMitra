# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2020-02-26 08:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20200226_0109'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='email',
            field=models.EmailField(default=django.utils.timezone.now, max_length=254),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='zip',
            field=models.IntegerField(null=True),
        ),
    ]
