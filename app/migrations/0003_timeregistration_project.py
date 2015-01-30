# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20150130_1401'),
    ]

    operations = [
        migrations.AddField(
            model_name='timeregistration',
            name='project',
            field=models.CharField(default='ProjectDefault', max_length=50),
            preserve_default=False,
        ),
    ]
