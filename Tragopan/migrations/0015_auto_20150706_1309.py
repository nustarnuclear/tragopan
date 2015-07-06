# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Tragopan', '0014_auto_20150706_1219'),
    ]

    operations = [
        migrations.AddField(
            model_name='reactormodel',
            name='incore_instrument_position',
            field=models.ManyToManyField(to='Tragopan.ReactorPosition', related_name='incore_instrument_position'),
        ),
        migrations.AddField(
            model_name='reactormodel',
            name='thermal_couple_position',
            field=models.ManyToManyField(to='Tragopan.ReactorPosition', related_name='thermal_couple_position'),
        ),
    ]
