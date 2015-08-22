# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20150822_1751'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workplace',
            name='city',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='workplace',
            name='country',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='workplace',
            name='created_at',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='workplace',
            name='state',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='workplace',
            name='website',
            field=models.TextField(null=True, blank=True),
        ),
    ]
