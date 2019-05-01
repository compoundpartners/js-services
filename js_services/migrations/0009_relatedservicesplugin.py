# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-26 06:10
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import djangocms_icon.fields
import filer.fields.image
import sortedm2m.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.FILER_IMAGE_MODEL),
        #('js_companies', '0002_auto_20190417_0522'),
        ('aldryn_people', '0034_relatedpeopleplugin_related_companies'),
        ('aldryn_categories', '0007_categorytranslation_landing_page'),
        ('cms', '0020_old_tree_cleanup'),
        ('js_services', '0008_service_sections'),
    ]

    operations = [
        migrations.CreateModel(
            name='RelatedServicesPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='+', serialize=False, to='cms.CMSPlugin')),
                ('title', models.CharField(blank=True, max_length=255, verbose_name='Title')),
                ('icon', djangocms_icon.fields.Icon(blank=True, default='fa-', max_length=255, verbose_name='Icon')),
                ('count', models.PositiveSmallIntegerField(verbose_name='Number services')),
                ('layout', models.CharField(max_length=30, verbose_name='layout')),
                ('image', filer.fields.image.FilerImageField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.FILER_IMAGE_MODEL)),
                ('related_categories', sortedm2m.fields.SortedManyToManyField(blank=True, help_text=None, to='aldryn_categories.Category', verbose_name='related categories')),
                #('related_companies', sortedm2m.fields.SortedManyToManyField(blank=True, help_text=None, to='js_companies.Company', verbose_name='related companies')),
                ('related_people', sortedm2m.fields.SortedManyToManyField(blank=True, help_text=None, to='aldryn_people.Person', verbose_name='key people')),
                ('related_sections', sortedm2m.fields.SortedManyToManyField(blank=True, help_text=None, to='js_services.ServicesConfig', verbose_name='related sections')),
                ('related_services', sortedm2m.fields.SortedManyToManyField(blank=True, help_text=None, to='js_services.Service', verbose_name='related services')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
