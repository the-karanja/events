# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-07 11:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='students',
            old_name='CLass',
            new_name='Class',
        ),
    ]