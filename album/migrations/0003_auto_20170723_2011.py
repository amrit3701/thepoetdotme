# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-23 20:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0002_auto_20170302_1434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='file',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
