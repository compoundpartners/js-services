# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-02-18 12:37
from __future__ import unicode_literals

from django.db import migrations
import sortedm2m.fields


class Migration(migrations.Migration):

    dependencies = [
        ('js_services', '0004_auto_20190213_0944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='related',
            field=sortedm2m.fields.SortedManyToManyField(blank=True, help_text=None, related_name='related_rel_+', to='js_services.Service', verbose_name='related services'),
        ),
    ]
