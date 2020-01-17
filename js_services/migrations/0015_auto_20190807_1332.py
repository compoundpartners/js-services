# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-08-07 13:32
from __future__ import unicode_literals

import cms.models.fields
from django.db import migrations
import django.db.models.deletion
import js_color_picker.fields
import parler.fields


class Migration(migrations.Migration):

    dependencies = [
        ('js_services', '0014_service_related_articles_placeholder'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='banner',
            field=cms.models.fields.PlaceholderField(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='service_banner', slotname='service_banner', to='cms.Placeholder'),
        ),
    ]