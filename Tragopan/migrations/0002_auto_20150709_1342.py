# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Tragopan', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fuelelementmap',
            name='fuel_assembly_position',
            field=models.OneToOneField(to='Tragopan.FuelAssemblyPosition'),
        ),
        migrations.AlterField(
            model_name='guidtubemap',
            name='fuel_assembly_position',
            field=models.OneToOneField(to='Tragopan.FuelAssemblyPosition'),
        ),
        migrations.AlterField(
            model_name='instrumenttubeposition',
            name='fuel_assembly_position',
            field=models.OneToOneField(to='Tragopan.FuelAssemblyPosition'),
        ),
    ]
