# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-29 13:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0015_photo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='photo',
            options={},
        ),
        migrations.RemoveField(
            model_name='photo',
            name='description',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='uploaded_at',
        ),
        migrations.AlterField(
            model_name='photo',
            name='file',
            field=models.ImageField(blank=True, upload_to='uploaded_images'),
        ),
    ]
