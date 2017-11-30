# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-30 18:28
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ideas', '0008_auto_20171130_1927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idea',
            name='last_bidder',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='potential_buyer', to=settings.AUTH_USER_MODEL),
        ),
    ]
