# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-29 13:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Projects', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='title',
            new_name='project_text',
        ),
    ]
