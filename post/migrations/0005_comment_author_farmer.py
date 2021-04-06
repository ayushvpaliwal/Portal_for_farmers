# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-31 17:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0002_auto_20171031_1709'),
        ('post', '0004_post_image_db'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='author_farmer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='User.Farmer'),
        ),
    ]