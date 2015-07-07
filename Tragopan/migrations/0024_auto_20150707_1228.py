# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('Tragopan', '0023_auto_20150707_1221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='corebaffle',
            name='weight',
            field=models.DecimalField(decimal_places=3, null=True, help_text='unit:Kg', max_digits=7, validators=[django.core.validators.MinValueValidator(0)], blank=True),
        ),
        migrations.AlterField(
            model_name='corelowerplate',
            name='weight',
            field=models.DecimalField(max_digits=7, decimal_places=3, validators=[django.core.validators.MinValueValidator(0)], help_text='unit:Kg'),
        ),
        migrations.AlterField(
            model_name='coreupperplate',
            name='weight',
            field=models.DecimalField(max_digits=7, decimal_places=3, validators=[django.core.validators.MinValueValidator(0)], help_text='unit:Kg'),
        ),
        migrations.AlterField(
            model_name='materialattribute',
            name='density',
            field=models.DecimalField(max_digits=20, decimal_places=10, help_text='unit:g/cm3'),
        ),
        migrations.AlterField(
            model_name='materialattribute',
            name='expansion_coefficient',
            field=models.DecimalField(max_digits=20, decimal_places=10, null=True, help_text='m/K', blank=True),
        ),
        migrations.AlterField(
            model_name='materialattribute',
            name='heat_capacity',
            field=models.DecimalField(max_digits=20, decimal_places=10, null=True, help_text='J/kg*K', blank=True),
        ),
        migrations.AlterField(
            model_name='materialattribute',
            name='thermal_conductivity',
            field=models.DecimalField(max_digits=20, decimal_places=10, null=True, help_text='W/m*K', blank=True),
        ),
        migrations.AlterField(
            model_name='materialcomposition',
            name='weight_percent',
            field=models.DecimalField(max_digits=9, decimal_places=6, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)], help_text='unit:%'),
        ),
        migrations.AlterField(
            model_name='materialnuclide',
            name='weight_percent',
            field=models.DecimalField(max_digits=9, decimal_places=6, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)], help_text='unit:%'),
        ),
        migrations.AlterField(
            model_name='nuclide',
            name='abundance',
            field=models.DecimalField(max_digits=9, decimal_places=6, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)], help_text='unit:%'),
        ),
        migrations.AlterField(
            model_name='unitparameter',
            name='best_estimated_cool_vol_flow_rate',
            field=models.DecimalField(max_digits=20, decimal_places=10, validators=[django.core.validators.MinValueValidator(0)], help_text='unit:m3/h'),
        ),
    ]
