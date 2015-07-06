# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Tragopan', '0019_auto_20150706_1413'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reactormodel',
            name='incore_instrument_position',
            field=models.ManyToManyField(to='Tragopan.ReactorPosition', blank=True, related_name='incore_instrument_position', db_table='incore_instrument_map'),
        ),
        migrations.AlterField(
            model_name='reactormodel',
            name='thermal_couple_position',
            field=models.ManyToManyField(to='Tragopan.ReactorPosition', blank=True, related_name='thermal_couple_position', db_table='thermal_couple_map'),
        ),
    ]
