# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('Tragopan', '0024_auto_20150707_1228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='materialattribute',
            name='density',
            field=models.DecimalField(max_digits=15, help_text='unit:g/cm3', decimal_places=5),
        ),
        migrations.AlterField(
            model_name='materialattribute',
            name='expansion_coefficient',
            field=models.DecimalField(null=True, decimal_places=5, max_digits=15, help_text='m/K', blank=True),
        ),
        migrations.AlterField(
            model_name='materialattribute',
            name='heat_capacity',
            field=models.DecimalField(null=True, decimal_places=5, max_digits=15, help_text='J/kg*K', blank=True),
        ),
        migrations.AlterField(
            model_name='materialattribute',
            name='thermal_conductivity',
            field=models.DecimalField(null=True, decimal_places=5, max_digits=15, help_text='W/m*K', blank=True),
        ),
        migrations.AlterField(
            model_name='unitparameter',
            name='HFP_cool_inlet_temp',
            field=models.DecimalField(validators=[django.core.validators.MinValueValidator(0)], max_digits=15, help_text='unit:K', decimal_places=5),
        ),
        migrations.AlterField(
            model_name='unitparameter',
            name='HFP_core_ave_cool_temp',
            field=models.DecimalField(validators=[django.core.validators.MinValueValidator(0)], max_digits=15, help_text='unit:K', decimal_places=5),
        ),
        migrations.AlterField(
            model_name='unitparameter',
            name='HZP_cool_inlet_temp',
            field=models.DecimalField(validators=[django.core.validators.MinValueValidator(0)], max_digits=15, help_text='unit:K', decimal_places=5),
        ),
        migrations.AlterField(
            model_name='unitparameter',
            name='ave_linear_power_density',
            field=models.DecimalField(validators=[django.core.validators.MinValueValidator(0)], max_digits=15, help_text='unit:KW/m', decimal_places=5),
        ),
        migrations.AlterField(
            model_name='unitparameter',
            name='ave_mass_power_density',
            field=models.DecimalField(validators=[django.core.validators.MinValueValidator(0)], max_digits=15, help_text='unit:KW/Kg (fuel)', decimal_places=5),
        ),
        migrations.AlterField(
            model_name='unitparameter',
            name='ave_vol_power_density',
            field=models.DecimalField(validators=[django.core.validators.MinValueValidator(0)], max_digits=15, help_text='unit:KW/L', decimal_places=5),
        ),
        migrations.AlterField(
            model_name='unitparameter',
            name='best_estimated_cool_vol_flow_rate',
            field=models.DecimalField(validators=[django.core.validators.MinValueValidator(0)], max_digits=15, help_text='unit:m3/h', decimal_places=5),
        ),
        migrations.AlterField(
            model_name='unitparameter',
            name='cold_state_cool_temp',
            field=models.DecimalField(validators=[django.core.validators.MinValueValidator(0)], max_digits=15, help_text='unit:K', decimal_places=5),
        ),
        migrations.AlterField(
            model_name='unitparameter',
            name='mid_power_cool_inlet_temp',
            field=models.DecimalField(validators=[django.core.validators.MinValueValidator(0)], blank=True, null=True, max_digits=15, help_text='unit:K', decimal_places=5),
        ),
        migrations.AlterField(
            model_name='unitparameter',
            name='primary_system_pressure',
            field=models.DecimalField(validators=[django.core.validators.MinValueValidator(0)], max_digits=15, help_text='unit:MPa', decimal_places=5),
        ),
    ]
