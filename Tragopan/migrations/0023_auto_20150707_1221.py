# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('Tragopan', '0022_auto_20150707_1207'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='unitparameter',
            name='best_estimated_cool_mass_flow_rate',
        ),
        migrations.AlterField(
            model_name='unitparameter',
            name='ave_linear_power_density',
            field=models.DecimalField(max_digits=20, validators=[django.core.validators.MinValueValidator(0)], help_text='unit:KW/m', decimal_places=10),
        ),
        migrations.AlterField(
            model_name='unitparameter',
            name='ave_mass_power_density',
            field=models.DecimalField(max_digits=20, validators=[django.core.validators.MinValueValidator(0)], help_text='unit:KW/Kg (fuel)', decimal_places=10),
        ),
        migrations.AlterField(
            model_name='unitparameter',
            name='ave_vol_power_density',
            field=models.DecimalField(max_digits=20, validators=[django.core.validators.MinValueValidator(0)], help_text='unit:KW/L', decimal_places=10),
        ),
        migrations.AlterField(
            model_name='unitparameter',
            name='bypass_flow_fraction',
            field=models.DecimalField(max_digits=9, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)], help_text='unit:%', decimal_places=6),
        ),
        migrations.AlterField(
            model_name='unitparameter',
            name='heat_fraction_in_fuel',
            field=models.DecimalField(max_digits=9, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)], help_text='unit:%', decimal_places=6),
        ),
    ]
