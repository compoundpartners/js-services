# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-01 09:14
from __future__ import unicode_literals

from django.db import migrations
import sortedm2m.fields


class Migration(migrations.Migration):

    dependencies = [
        #('js_companies', '0001_initial'),
        ('js_services', '0006_auto_20190326_1107'),
    ]

    operations = [
        #migrations.AddField(
            #model_name='service',
            #name='companies',
            #field=sortedm2m.fields.SortedManyToManyField(blank=True, help_text=None, to='js_companies.Company', verbose_name='companies'),
        #),
    ]
