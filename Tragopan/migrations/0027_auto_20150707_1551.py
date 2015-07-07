# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Tragopan', '0026_auto_20150707_1530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fuelassemblyloadingpattern',
            name='cycle',
            field=models.ForeignKey(to='Tragopan.Cycle', related_name='fuel_assembly_positions'),
        ),
    ]
