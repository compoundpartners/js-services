# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-26 11:07
from __future__ import unicode_literals

import cms.models.fields
from django.db import migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0020_old_tree_cleanup'),
        ('js_services', '0005_auto_20190218_1237'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='sidebar',
            field=cms.models.fields.PlaceholderField(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='service_sidebar', slotname='service_sidebar', to='cms.Placeholder'),
        ),
        migrations.AlterField(
            model_name='service',
            name='content',
            field=cms.models.fields.PlaceholderField(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='service_content', slotname='service_content', to='cms.Placeholder'),
        ),
    ]
