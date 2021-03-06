# -*- coding: utf-8 -*-
# Generated by Django 1.11.22 on 2019-07-09 23:15
from __future__ import unicode_literals

from django.db import migrations, models
import js_color_picker.fields


class Migration(migrations.Migration):

    dependencies = [
        ('js_services', '0012_auto_20190430_0804'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='nofollow',
            field=models.BooleanField(default=False, verbose_name='nofollow'),
        ),
        migrations.AddField(
            model_name='service',
            name='noindex',
            field=models.BooleanField(default=False, verbose_name='noindex'),
        ),
        migrations.AddField(
            model_name='service',
            name='show_on_sitemap',
            field=models.BooleanField(default=True, verbose_name='Show on sitemap'),
        ),
        migrations.AddField(
            model_name='service',
            name='show_on_xml_sitemap',
            field=models.BooleanField(default=True, verbose_name='Show on xml sitemap'),
        ),
        migrations.AlterField(
            model_name='relatedservicesplugin',
            name='background_color',
            field=js_color_picker.fields.RGBColorField(blank=True, colors={'#2B3B46': 'dark', '#323B50': 'grey', '#919FA6': 'cool grey', '#CBCBCB': 'medium-grey', '#FBDB4C': 'maize', '#f5f5f5': 'light-grey', '#ffffff': 'white'}, mode='choice', null=True, verbose_name='Background Color'),
        ),
    ]
