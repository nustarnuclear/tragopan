# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('Tragopan', '0013_vendor'),
    ]

    operations = [
        migrations.CreateModel(
            name='CoreBaffle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('time_inserted', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True)),
                ('gap_to_fuel', models.DecimalField(help_text='unit:cm', decimal_places=3, max_digits=7, validators=[django.core.validators.MinValueValidator(0)])),
                ('outer_diameter', models.DecimalField(help_text='unit:cm', decimal_places=3, max_digits=7, validators=[django.core.validators.MinValueValidator(0)])),
                ('thickness', models.DecimalField(blank=True, validators=[django.core.validators.MinValueValidator(0)], null=True, help_text='unit:cm', decimal_places=3, max_digits=7)),
                ('weight', models.DecimalField(blank=True, validators=[django.core.validators.MinValueValidator(0)], null=True, help_text='unit:KG', decimal_places=3, max_digits=7)),
                ('material', models.ForeignKey(to='Tragopan.Material')),
            ],
            options={
                'db_table': 'core_baffle',
            },
        ),
        migrations.CreateModel(
            name='CoreBarrel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('time_inserted', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True)),
                ('outer_diameter', models.DecimalField(help_text='unit:cm', decimal_places=3, max_digits=7, validators=[django.core.validators.MinValueValidator(0)])),
                ('inner_diameter', models.DecimalField(help_text='unit:cm', decimal_places=3, max_digits=7, validators=[django.core.validators.MinValueValidator(0)])),
                ('material', models.ForeignKey(to='Tragopan.Material')),
            ],
            options={
                'db_table': 'core_barrel',
            },
        ),
        migrations.CreateModel(
            name='CoreLowerPlate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('time_inserted', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True)),
                ('weight', models.DecimalField(help_text='unit:KG', decimal_places=3, max_digits=7, validators=[django.core.validators.MinValueValidator(0)])),
                ('material', models.ForeignKey(to='Tragopan.Material')),
            ],
            options={
                'db_table': 'core_lower_plate',
            },
        ),
        migrations.CreateModel(
            name='CoreUpperPlate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('time_inserted', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True)),
                ('type', models.CharField(choices=[('Upper', 'Upper'), ('Lower', 'Lower')], max_length=5)),
                ('weight', models.DecimalField(help_text='unit:KG', decimal_places=3, max_digits=7, validators=[django.core.validators.MinValueValidator(0)])),
                ('material', models.ForeignKey(to='Tragopan.Material')),
            ],
            options={
                'db_table': 'core_upper_plate',
            },
        ),
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('time_inserted', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True)),
                ('nameCH', models.CharField(max_length=40)),
                ('abbrCH', models.CharField(max_length=40)),
                ('nameEN', models.CharField(max_length=40)),
                ('abbrEN', models.CharField(max_length=40)),
            ],
            options={
                'db_table': 'plant',
            },
        ),
        migrations.CreateModel(
            name='PressureVessel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('time_inserted', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True)),
                ('outer_diameter', models.DecimalField(help_text='unit:cm', decimal_places=3, max_digits=7, validators=[django.core.validators.MinValueValidator(0)])),
                ('inner_diameter', models.DecimalField(help_text='unit:cm', decimal_places=3, max_digits=7, validators=[django.core.validators.MinValueValidator(0)])),
                ('weld_thickness', models.DecimalField(help_text='unit:cm', decimal_places=3, max_digits=7, validators=[django.core.validators.MinValueValidator(0)])),
                ('base_material', models.ForeignKey(to='Tragopan.Material', related_name='pressure_vessel_base')),
            ],
            options={
                'db_table': 'pressure_vessel',
            },
        ),
        migrations.CreateModel(
            name='PressureVesselInsulation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('time_inserted', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True)),
                ('outer_diameter', models.DecimalField(help_text='unit:cm', decimal_places=3, max_digits=7, validators=[django.core.validators.MinValueValidator(0)])),
                ('inner_diameter', models.DecimalField(help_text='unit:cm', decimal_places=3, max_digits=7, validators=[django.core.validators.MinValueValidator(0)])),
                ('material', models.ForeignKey(to='Tragopan.Material')),
            ],
            options={
                'db_table': 'pressure_vessel_insulation',
            },
        ),
        migrations.CreateModel(
            name='ReactorModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('time_inserted', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True)),
                ('model', models.CharField(max_length=50)),
                ('generation', models.CharField(choices=[('2', '2'), ('2+', '2+'), ('3', '3')], max_length=2)),
                ('reactor_type', models.CharField(choices=[('PWR', 'PWR'), ('BWR', 'BWR')], max_length=3)),
                ('geometry_type', models.CharField(choices=[('Cartesian', 'Cartesian'), ('Hexagonal', 'Hexagonal')], max_length=9)),
                ('row_symbol', models.CharField(choices=[('Number', 'Number'), ('Letter', 'Letter')], max_length=6)),
                ('column_symbol', models.CharField(choices=[('Number', 'Number'), ('Letter', 'Letter')], max_length=6)),
                ('num_loops', models.PositiveSmallIntegerField()),
                ('num_control_rod_mechanisms', models.PositiveSmallIntegerField()),
                ('core_equivalent_diameter', models.DecimalField(help_text='unit:cm', decimal_places=3, max_digits=7, validators=[django.core.validators.MinValueValidator(0)])),
                ('active_height', models.DecimalField(help_text='unit:cm', decimal_places=3, max_digits=7, validators=[django.core.validators.MinValueValidator(0)])),
                ('cold_state_assembly_pitch', models.DecimalField(help_text='unit:cm', decimal_places=3, max_digits=7, validators=[django.core.validators.MinValueValidator(0)])),
                ('hot_state_assembly_pitch', models.DecimalField(help_text='unit:cm', decimal_places=3, max_digits=7, validators=[django.core.validators.MinValueValidator(0)])),
            ],
            options={
                'db_table': 'reactor_model',
            },
        ),
        migrations.CreateModel(
            name='ReactorPosition',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('time_inserted', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True)),
                ('row', models.PositiveSmallIntegerField()),
                ('column', models.PositiveSmallIntegerField()),
                ('reactor_model', models.ForeignKey(to='Tragopan.ReactorModel')),
            ],
            options={
                'db_table': 'reactor_position',
            },
        ),
        migrations.CreateModel(
            name='RipPlate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('time_inserted', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True)),
                ('height', models.DecimalField(help_text='unit:cm', decimal_places=3, max_digits=7, validators=[django.core.validators.MinValueValidator(0)])),
                ('thickness', models.DecimalField(help_text='unit:cm', decimal_places=3, max_digits=7, validators=[django.core.validators.MinValueValidator(0)])),
                ('width', models.DecimalField(blank=True, validators=[django.core.validators.MinValueValidator(0)], null=True, help_text='unit:cm', decimal_places=3, max_digits=7)),
                ('core_baffle', models.OneToOneField(to='Tragopan.ReactorModel')),
                ('material', models.ForeignKey(to='Tragopan.Material')),
            ],
            options={
                'db_table': 'rip_plate',
            },
        ),
        migrations.CreateModel(
            name='ThermalShield',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('time_inserted', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True)),
                ('height', models.DecimalField(help_text='unit:cm', decimal_places=3, max_digits=7, validators=[django.core.validators.MinValueValidator(0)])),
                ('outer_diameter', models.DecimalField(help_text='unit:cm', decimal_places=3, max_digits=7, validators=[django.core.validators.MinValueValidator(0)])),
                ('inner_diameter', models.DecimalField(help_text='unit:cm', decimal_places=3, max_digits=7, validators=[django.core.validators.MinValueValidator(0)])),
                ('angle', models.DecimalField(help_text='unit:degree', decimal_places=3, max_digits=7, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(360)])),
                ('loc_height', models.DecimalField(help_text='unit:cm', decimal_places=3, max_digits=7, validators=[django.core.validators.MinValueValidator(0)])),
                ('loc_theta', models.DecimalField(help_text='unit:degree', decimal_places=3, max_digits=7, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(360)])),
                ('gap_to_barrel', models.DecimalField(help_text='unit:cm', decimal_places=3, max_digits=7, validators=[django.core.validators.MinValueValidator(0)])),
                ('material', models.ForeignKey(to='Tragopan.Material')),
                ('reactor_model', models.ForeignKey(to='Tragopan.ReactorModel')),
            ],
            options={
                'db_table': 'thermal_shield',
            },
        ),
        migrations.AddField(
            model_name='vendor',
            name='type',
            field=models.CharField(choices=[('Designer', 'Designer'), ('Manufacturer', 'Manufacturer'), ('Material', 'Material')], max_length=12, default='Designer'),
        ),
        migrations.AddField(
            model_name='thermalshield',
            name='vendor',
            field=models.ForeignKey(to='Tragopan.Vendor'),
        ),
        migrations.AddField(
            model_name='reactormodel',
            name='vendor',
            field=models.ForeignKey(to='Tragopan.Vendor'),
        ),
        migrations.AddField(
            model_name='pressurevesselinsulation',
            name='reactor_model',
            field=models.OneToOneField(to='Tragopan.ReactorModel'),
        ),
        migrations.AddField(
            model_name='pressurevesselinsulation',
            name='vendor',
            field=models.ForeignKey(to='Tragopan.Vendor'),
        ),
        migrations.AddField(
            model_name='pressurevessel',
            name='reactor_model',
            field=models.OneToOneField(to='Tragopan.ReactorModel'),
        ),
        migrations.AddField(
            model_name='pressurevessel',
            name='vendor',
            field=models.ForeignKey(to='Tragopan.Vendor'),
        ),
        migrations.AddField(
            model_name='pressurevessel',
            name='weld_material',
            field=models.ForeignKey(to='Tragopan.Material', related_name='pressure_vessel_weld'),
        ),
        migrations.AddField(
            model_name='coreupperplate',
            name='reactor_model',
            field=models.OneToOneField(to='Tragopan.ReactorModel'),
        ),
        migrations.AddField(
            model_name='coreupperplate',
            name='vendor',
            field=models.ForeignKey(to='Tragopan.Vendor'),
        ),
        migrations.AddField(
            model_name='corelowerplate',
            name='reactor_model',
            field=models.OneToOneField(to='Tragopan.ReactorModel'),
        ),
        migrations.AddField(
            model_name='corelowerplate',
            name='vendor',
            field=models.ForeignKey(to='Tragopan.Vendor'),
        ),
        migrations.AddField(
            model_name='corebarrel',
            name='reactor_model',
            field=models.OneToOneField(to='Tragopan.ReactorModel'),
        ),
        migrations.AddField(
            model_name='corebarrel',
            name='vendor',
            field=models.ForeignKey(to='Tragopan.Vendor'),
        ),
        migrations.AddField(
            model_name='corebaffle',
            name='reactor_model',
            field=models.OneToOneField(to='Tragopan.ReactorModel'),
        ),
        migrations.AddField(
            model_name='corebaffle',
            name='vendor',
            field=models.ForeignKey(to='Tragopan.Vendor'),
        ),
    ]
