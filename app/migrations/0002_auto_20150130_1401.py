# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timeregistration',
            name='registration_day',
            field=models.DateField(),
            preserve_default=True,
        ),
    ]
