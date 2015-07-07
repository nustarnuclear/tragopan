# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('Tragopan', '0025_auto_20150707_1238'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cycle',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('time_inserted', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True)),
                ('cycle', models.PositiveSmallIntegerField()),
                ('starting_date', models.DateField(help_text='Please use <b>YYYY-MM-DD<b> to input the date')),
                ('shutdown_date', models.DateField(help_text='Please use <b>YYYY-MM-DD<b> to input the date')),
                ('cycle_length', models.DecimalField(validators=[django.core.validators.MinValueValidator(0)], decimal_places=3, max_digits=7, help_text='unit:EFPD')),
                ('num_unplanned_shutdowns', models.PositiveSmallIntegerField()),
                ('num_periodical_tests', models.PositiveSmallIntegerField()),
                ('unit', models.ForeignKey(to='Tragopan.UnitParameter')),
            ],
            options={
                'db_table': 'cycle',
            },
        ),
        migrations.CreateModel(
            name='FuelAssemblyLoadingPattern',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('time_inserted', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True)),
                ('rotation_degree', models.CharField(max_length=3, choices=[('0', '0'), ('90', '90'), ('180', '180'), ('270', '270')], default='0')),
                ('cycle_burnup', models.DecimalField(max_digits=15, null=True, validators=[django.core.validators.MinValueValidator(0)], decimal_places=5, blank=True, help_text='MWd/tU')),
                ('cycle', models.ForeignKey(to='Tragopan.Cycle')),
            ],
            options={
                'db_table': 'fuel_assembly_loading_pattern',
            },
        ),
        migrations.CreateModel(
            name='FuelAssemblyModel',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('time_inserted', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True)),
                ('model', models.CharField(max_length=5, choices=[('AFA2G', 'AFA2G'), ('AFA3G', 'AFA3G')])),
                ('overall_length', models.DecimalField(validators=[django.core.validators.MinValueValidator(0)], decimal_places=3, max_digits=7, help_text='unit:cm')),
                ('side_length', models.DecimalField(validators=[django.core.validators.MinValueValidator(0)], decimal_places=3, max_digits=7, help_text='unit:cm')),
                ('pin_pitch', models.DecimalField(validators=[django.core.validators.MinValueValidator(0)], decimal_places=3, max_digits=7, help_text='unit:cm')),
                ('lower_gap', models.DecimalField(validators=[django.core.validators.MinValueValidator(0)], decimal_places=3, max_digits=7, help_text='unit:cm')),
                ('upper_gap', models.DecimalField(validators=[django.core.validators.MinValueValidator(0)], decimal_places=3, max_digits=7, help_text='unit:cm')),
                ('licensed_max_discharge_BU', models.DecimalField(max_digits=15, null=True, validators=[django.core.validators.MinValueValidator(0)], decimal_places=5, blank=True, help_text='MWd/tU')),
                ('licensed_pin_discharge_BU', models.DecimalField(max_digits=15, null=True, validators=[django.core.validators.MinValueValidator(0)], decimal_places=5, blank=True, help_text='MWd/tU')),
            ],
            options={
                'db_table': 'fuel_assembly_model',
            },
        ),
        migrations.CreateModel(
            name='FuelAssemblyPosition',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('time_inserted', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True)),
                ('row', models.PositiveSmallIntegerField()),
                ('column', models.PositiveSmallIntegerField()),
                ('fuel_assembly_model', models.ForeignKey(related_name='positions', to='Tragopan.FuelAssemblyModel', related_query_name='position')),
            ],
            options={
                'db_table': 'fuel_assembly_position',
            },
        ),
        migrations.CreateModel(
            name='FuelAssemblyRepository',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('time_inserted', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True)),
                ('PN', models.CharField(max_length=50, unique=True)),
                ('batch_number', models.PositiveSmallIntegerField()),
                ('manufacturing_date', models.DateField(help_text='Please use <b>YYYY-MM-DD<b> to input the date')),
                ('arrival_date', models.DateField(help_text='Please use <b>YYYY-MM-DD<b> to input the date')),
                ('availability', models.NullBooleanField(verbose_name='available now?', default='True')),
                ('model', models.ForeignKey(to='Tragopan.FuelAssemblyModel')),
                ('plant', models.ForeignKey(to='Tragopan.Plant')),
                ('vendor', models.ForeignKey(to='Tragopan.Vendor')),
            ],
            options={
                'db_table': 'fuel_assembly_repository',
            },
        ),
        migrations.CreateModel(
            name='Grid',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('time_inserted', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True)),
                ('model', models.CharField(max_length=40)),
                ('sleeve_weight', models.DecimalField(validators=[django.core.validators.MinValueValidator(0)], decimal_places=5, max_digits=15, help_text='g')),
                ('sleeve_thickness', models.DecimalField(validators=[django.core.validators.MinValueValidator(0)], decimal_places=5, max_digits=10, help_text='cm')),
                ('spring_weight', models.DecimalField(validators=[django.core.validators.MinValueValidator(0)], decimal_places=5, max_digits=15, help_text='g')),
                ('spring_thickness', models.DecimalField(validators=[django.core.validators.MinValueValidator(0)], decimal_places=5, max_digits=10, help_text='cm')),
                ('functionality', models.CharField(max_length=5, choices=[('blend', 'blend'), ('fix', 'fix')], default='fix')),
                ('fuel_assembly_model', models.ForeignKey(to='Tragopan.FuelAssemblyModel')),
                ('sleeve_material', models.ForeignKey(related_name='grid_sleeves', to='Tragopan.Material', related_query_name='grid_sleeve')),
                ('spring_material', models.ForeignKey(related_name='grid_springs', to='Tragopan.Material', related_query_name='grid_spring')),
                ('vendor', models.ForeignKey(to='Tragopan.Vendor')),
            ],
            options={
                'db_table': 'grid',
            },
        ),
        migrations.CreateModel(
            name='GridPosition',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('time_inserted', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True)),
                ('height', models.DecimalField(validators=[django.core.validators.MinValueValidator(0)], decimal_places=3, max_digits=7, help_text='unit:cm')),
                ('fuel_assembly_model', models.ForeignKey(to='Tragopan.FuelAssemblyModel')),
                ('grid', models.ForeignKey(to='Tragopan.Grid')),
            ],
            options={
                'db_table': 'grid_position',
            },
        ),
        migrations.CreateModel(
            name='GuidTube',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('time_inserted', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True)),
                ('outer_diameter', models.DecimalField(validators=[django.core.validators.MinValueValidator(0)], decimal_places=3, max_digits=7, help_text='unit:cm')),
                ('inner_diameter', models.DecimalField(validators=[django.core.validators.MinValueValidator(0)], decimal_places=3, max_digits=7, help_text='unit:cm')),
                ('fuel_assembly_model', models.ForeignKey(to='Tragopan.FuelAssemblyModel')),
                ('material', models.ForeignKey(to='Tragopan.Material')),
                ('vendor', models.ForeignKey(to='Tragopan.Vendor')),
            ],
            options={
                'db_table': 'guid_tube',
            },
        ),
        migrations.AddField(
            model_name='fuelassemblymodel',
            name='grid_position',
            field=models.ManyToManyField(related_name='grid_position', to='Tragopan.Grid', through='Tragopan.GridPosition'),
        ),
        migrations.AddField(
            model_name='fuelassemblymodel',
            name='guid_tube_map',
            field=models.ManyToManyField(db_table='guid_tube_map', related_name='guid_tube_map', to='Tragopan.FuelAssemblyPosition'),
        ),
        migrations.AddField(
            model_name='fuelassemblymodel',
            name='vendor',
            field=models.ForeignKey(to='Tragopan.Vendor'),
        ),
        migrations.AddField(
            model_name='fuelassemblyloadingpattern',
            name='fuel_assembly',
            field=models.ForeignKey(to='Tragopan.FuelAssemblyRepository'),
        ),
        migrations.AddField(
            model_name='fuelassemblyloadingpattern',
            name='reactor_position',
            field=models.ForeignKey(to='Tragopan.ReactorPosition'),
        ),
        migrations.AlterUniqueTogether(
            name='fuelassemblyposition',
            unique_together=set([('fuel_assembly_model', 'row', 'column')]),
        ),
        migrations.AlterUniqueTogether(
            name='fuelassemblyloadingpattern',
            unique_together=set([('cycle', 'reactor_position')]),
        ),
        migrations.AlterUniqueTogether(
            name='cycle',
            unique_together=set([('cycle', 'unit')]),
        ),
    ]
