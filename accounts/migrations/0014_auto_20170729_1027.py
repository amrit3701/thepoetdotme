# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-29 10:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_profilephoto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profilephoto',
            name='user',
        ),
        migrations.DeleteModel(
            name='ProfilePhoto',
        ),
    ]
