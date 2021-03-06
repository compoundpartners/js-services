# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-29 17:05
from __future__ import unicode_literals

from django.db import migrations
import djangocms_icon.fields


def forwards(apps, schema_editor):
    RelatedServicesPlugin = apps.get_model('js_services', 'RelatedServicesPlugin')
    for s in RelatedServicesPlugin.objects.all():
        if s.icon == 'fa-':
            s.icon = ''
            s.save()

def backward(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('js_services', '0010_auto_20190427_0723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='relatedservicesplugin',
            name='icon',
            field=djangocms_icon.fields.Icon(blank=True, default='', max_length=255, verbose_name='Icon'),
        ),
        migrations.RunPython(forwards, backward),
    ]
