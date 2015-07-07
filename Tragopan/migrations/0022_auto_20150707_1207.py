# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('Tragopan', '0021_auto_20150706_1926'),
    ]

    operations = [
        migrations.CreateModel(
            name='UnitParameter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('time_inserted', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True)),
                ('unit', models.PositiveSmallIntegerField()),
                ('electric_power', models.DecimalField(help_text='unit:MW', max_digits=10, validators=[django.core.validators.MinValueValidator(0)], decimal_places=3)),
                ('thermal_power', models.DecimalField(help_text='unit:MW', max_digits=10, validators=[django.core.validators.MinValueValidator(0)], decimal_places=3)),
                ('heat_fraction_in_fuel', models.DecimalField(help_text='unit:percentage', max_digits=9, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)], decimal_places=6)),
                ('primary_system_pressure', models.DecimalField(help_text='unit:MPa', max_digits=20, validators=[django.core.validators.MinValueValidator(0)], decimal_places=10)),
                ('ave_linear_power_density', models.DecimalField(help_text='unit:W_per_cm', max_digits=20, validators=[django.core.validators.MinValueValidator(0)], decimal_places=10)),
                ('ave_vol_power_density', models.DecimalField(help_text='unit:KW_per_L', max_digits=20, validators=[django.core.validators.MinValueValidator(0)], decimal_places=10)),
                ('ave_mass_power_density', models.DecimalField(help_text='unit:W_per_gfuel', max_digits=20, validators=[django.core.validators.MinValueValidator(0)], decimal_places=10)),
                ('best_estimated_cool_vol_flow_rate', models.DecimalField(help_text='unit:m3_per_h', max_digits=20, validators=[django.core.validators.MinValueValidator(0)], decimal_places=10)),
                ('best_estimated_cool_mass_flow_rate', models.DecimalField(help_text='unit:ton_per_h', max_digits=20, validators=[django.core.validators.MinValueValidator(0)], decimal_places=10)),
                ('bypass_flow_fraction', models.DecimalField(help_text='unit:percentage', max_digits=9, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)], decimal_places=6)),
                ('cold_state_cool_temp', models.DecimalField(help_text='unit:K', max_digits=20, validators=[django.core.validators.MinValueValidator(0)], decimal_places=10)),
                ('HZP_cool_inlet_temp', models.DecimalField(help_text='unit:K', max_digits=20, validators=[django.core.validators.MinValueValidator(0)], decimal_places=10)),
                ('HFP_cool_inlet_temp', models.DecimalField(help_text='unit:K', max_digits=20, validators=[django.core.validators.MinValueValidator(0)], decimal_places=10)),
                ('HFP_core_ave_cool_temp', models.DecimalField(help_text='unit:K', max_digits=20, validators=[django.core.validators.MinValueValidator(0)], decimal_places=10)),
                ('mid_power_cool_inlet_temp', models.DecimalField(max_digits=20, validators=[django.core.validators.MinValueValidator(0)], decimal_places=10, blank=True, help_text='unit:K', null=True)),
                ('plant', models.ForeignKey(to='Tragopan.Plant')),
                ('reactor_model', models.ForeignKey(to='Tragopan.ReactorModel')),
            ],
            options={
                'db_table': 'unit_parameter',
            },
        ),
        migrations.AlterUniqueTogether(
            name='unitparameter',
            unique_together=set([('plant', 'unit')]),
        ),
    ]
