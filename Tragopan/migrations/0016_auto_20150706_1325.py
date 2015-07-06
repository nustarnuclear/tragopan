# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Tragopan', '0015_auto_20150706_1309'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coreupperplate',
            name='type',
        ),
        migrations.AlterField(
            model_name='reactormodel',
            name='incore_instrument_position',
            field=models.ManyToManyField(related_name='incore_instrument_position', blank=True, to='Tragopan.ReactorPosition'),
        ),
        migrations.AlterField(
            model_name='reactormodel',
            name='thermal_couple_position',
            field=models.ManyToManyField(related_name='thermal_couple_position', blank=True, to='Tragopan.ReactorPosition'),
        ),
    ]
