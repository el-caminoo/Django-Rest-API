# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-01-09 10:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_visitor_reason'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitor',
            name='reason',
            field=models.TextField(max_length=100, null=True),
        ),
    ]