# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-14 10:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Projects', '0004_auto_20160314_1136'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='project_text',
            new_name='title',
        ),
    ]