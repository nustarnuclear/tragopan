# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CladdingTube',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('time_inserted', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True)),
                ('outer_diameter', models.DecimalField(help_text='unit:cm', max_digits=7, decimal_places=3, validators=[django.core.validators.MinValueValidator(0)])),
                ('inner_diameter', models.DecimalField(help_text='unit:cm', max_digits=7, decimal_places=3, validators=[django.core.validators.MinValueValidator(0)])),
                ('roughness', models.DecimalField(help_text='unit:cm', max_digits=7, decimal_places=6, validators=[django.core.validators.MinValueValidator(0)], null=True, blank=True)),
            ],
            options={
                'db_table': 'cladding_tube',
            },
        ),
        migrations.CreateModel(
            name='CoreBaffle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('time_inserted', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True)),
                ('gap_to_fuel', models.DecimalField(help_text='unit:cm', max_digits=7, decimal_places=3, validators=[django.core.validators.MinValueValidator(0)])),
                ('outer_diameter', models.DecimalField(help_text='unit:cm', max_digits=7, decimal_places=3, validators=[django.core.validators.MinValueValidator(0)])),
                ('thickness', models.DecimalField(help_text='unit:cm', max_digits=7, decimal_places=3, validators=[django.core.validators.MinValueValidator(0)], null=True, blank=True)),
                ('weight', models.DecimalField(help_text='unit:Kg', max_digits=7, decimal_places=3, validators=[django.core.validators.MinValueValidator(0)], null=True, blank=True)),
            ],
            options={
                'db_table': 'core_baffle',
            },
        ),
        migrations.CreateModel(
            name='CoreBarrel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('time_inserted', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True)),
                ('outer_diameter', models.DecimalField(help_text='unit:cm', max_digits=7, decimal_places=3, validators=[django.core.validators.MinValueValidator(0)])),
                ('inner_diameter', models.DecimalField(help_text='unit:cm', max_digits=7, decimal_places=3, validators=[django.core.validators.MinValueValidator(0)])),
            ],
            options={
                'db_table': 'core_barrel',
            },
        ),
        migrations.CreateModel(
            name='CoreLowerPlate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('time_inserted', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True)),
                ('weight', models.DecimalField(help_text='unit:Kg', max_digits=7, decimal_places=3, validators=[django.core.validators.MinValueValidator(0)])),
            ],
            options={
                'db_table': 'core_lower_plate',
            },
        ),
        migrations.CreateModel(
            name='CoreUpperPlate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('time_inserted', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True)),
                ('weight', models.DecimalField(help_text='unit:Kg', max_digits=7, decimal_places=3, validators=[django.core.validators.MinValueValidator(0)])),
            ],
            options={
                'db_table': 'core_upper_plate',
            },
        ),
        migrations.CreateModel(
            name='Cycle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('time_inserted', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True)),
                ('cycle', models.PositiveSmallIntegerField()),
                ('starting_date', models.DateField(help_text='Please use <b>YYYY-MM-DD<b> to input the date')),
                ('shutdown_date', models.DateField(help_text='Please use <b>YYYY-MM-DD<b> to input the date')),
                ('cycle_length', models.DecimalField(help_text='unit:EFPD', max_digits=7, decimal_places=3, validators=[django.core.validators.MinValueValidator(0)])),
                ('num_unplanned_shutdowns', models.PositiveSmallIntegerField()),
                ('num_periodical_tests', models.PositiveSmallIntegerField()),
            ],
            options={
                'db_table': 'cycle',
            },
        ),
        migrations.CreateModel(
            name='Element',
            fields=[
                ('time_inserted', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True)),
                ('atomic_number', models.AutoField(primary_key=True, serialize=False)),
                ('symbol', models.CharField(max_length=8, unique=True)),
                ('nameCH', models.CharField(max_length=8)),
                ('nameEN', models.CharField(max_length=40)),
                ('reference', models.CharField(default='IUPAC', max_length=80)),
            ],
            options={
                'db_table': 'element',
                'ordering': ['atomic_number'],
            },
        ),
        migrations.CreateModel(
            name='FakeFuelElementType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('time_inserted', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True)),
                ('overall_length', models.DecimalField(help_text='unit:cm', max_digits=7, decimal_places=3, validators=[django.core.validators.MinValueValidator(0)])),
                ('outer_diameter', models.DecimalField(help_text='unit:cm', max_digits=7, decimal_places=3, validators=[django.core.validators.MinValueValidator(0)])),
                ('inner_diameter', models.DecimalField(help_text='unit:cm', max_digits=7, decimal_places=3, validators=[django.core.validators.MinValueValidator(0)])),
                ('pellet_outer_diameter', models.DecimalField(help_text='unit:cm', max_digits=7, decimal_places=3, validators=[django.core.validators.MinValueValidator(0)])),
                ('pellet_height', models.DecimalField(help_text='unit:cm', max_digits=7, decimal_places=3, validators=[django.core.validators.MinValueValidator(0)])),
            ],
            options={
                'db_table': 'fake_fuel_element_type',
            },
        ),
        migrations.CreateModel(
            name='FuelAssemblyLoadingPattern',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('time_inserted', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True)),
                ('rotation_degree', models.CharField(default='0', max_length=3, choices=[('0', '0'), ('90', '90'), ('180', '180'), ('270', '270')])),
                ('cycle', models.ForeignKey(to='Tragopan.Cycle', related_name='fuel_assembly_positions')),
            ],
            options={
                'db_table': 'fuel_assembly_loading_pattern',
            },
        ),
        migrations.CreateModel(
            name='FuelAssemblyModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('time_inserted', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True)),
                ('model', models.CharField(max_length=5, choices=[('AFA2G', 'AFA2G'), ('AFA3G', 'AFA3G')])),
                ('overall_length', models.DecimalField(help_text='unit:cm', max_digits=7, decimal_places=3, validators=[django.core.validators.MinValueValidator(0)])),
                ('side_length', models.DecimalField(help_text='unit:cm', max_digits=7, decimal_places=3, validators=[django.core.validators.MinValueValidator(0)])),
                ('pin_pitch', models.DecimalField(help_text='unit:cm', max_digits=7, decimal_places=3, validators=[django.core.validators.MinValueValidator(0)])),
                ('lower_gap', models.DecimalField(help_text='unit:cm', max_digits=7, decimal_places=3, validators=[django.core.validators.MinValueValidator(0)])),
                ('upper_gap', models.DecimalField(help_text='unit:cm', max_digits=7, decimal_places=3, validators=[django.core.validators.MinValueValidator(0)])),
                ('licensed_max_discharge_BU', models.DecimalField(help_text='MWd/tU', max_digits=15, decimal_places=5, validators=[django.core.validators.MinValueValidator(0)], null=True, blank=True)),
                ('licensed_pin_discharge_BU', models.DecimalField(help_text='MWd/tU', max_digits=15, decimal_places=5, validators=[django.core.validators.MinValueValidator(0)], null=True, blank=True)),
            ],
            options={
                'db_table': 'fuel_assembly_model',
            },
        ),
        migrations.CreateModel(
            name='FuelAssemblyPosition',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('time_inserted', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True)),
                ('row', models.PositiveSmallIntegerField()),
                ('column', models.PositiveSmallIntegerField()),
                ('fuel_assembly_model', models.ForeignKey(related_query_name='position', related_name='positions', to='Tragopan.FuelAssemblyModel')),
            ],
            options={
                'db_table': 'fuel_assembly_position',
            },
        ),
        migrations.CreateModel(
            name='FuelAssemblyRepository',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('time_inserted', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True)),
                ('PN', models.CharField(max_length=50, unique=True)),
                ('batch_number', models.PositiveSmallIntegerField()),
                ('manufacturing_date', models.DateField(help_text='Please use <b>YYYY-MM-DD<b> to input the date')),
                ('arrival_date', models.DateField(help_text='Please use <b>YYYY-MM-DD<b> to input the date')),
                ('model', models.ForeignKey(to='Tragopan.FuelAssemblyModel')),
            ],
            options={
                'db_table': 'fuel_assembly_repository',
            },
        ),
        migrations.CreateModel(
            name='FuelElementMap',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('time_inserted', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True)),
                ('fuel_assembly_position', models.ForeignKey(to='Tragopan.FuelAssemblyPosition')),
            ],
            options={
                'db_table': 'fuel_element_map',
            },
        ),
        migrations.CreateModel(
            name='FuelElementPelletLoadingScheme',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('time_inserted', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True)),
                ('order', models.PositiveSmallIntegerField()),
            ],
            options={
                'db_table': 'fuel_element_pellet_loading_scheme',
            },
        ),
        migrations.CreateModel(
            name='FuelElementType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('time_inserted', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True)),
                ('overall_length', models.DecimalField(help_text='unit:cm', max_digits=7, decimal_places=3, validators=[django.core.validators.MinValueValidator(0)])),
                ('active_length', models.DecimalField(help_text='unit:cm', max_digits=7, decimal_places=3, validators=[django.core.validators.MinValueValidator(0)])),
                ('plenum_length', models.DecimalField(help_text='unit:cm', max_digits=7, decimal_places=3, validators=[django.core.validators.MinValueValidator(0)])),
                ('filling_gas_pressure', models.DecimalField(help_text='unit:MPa', max_digits=10, decimal_places=5, validators=[django.core.validators.MinValueValidator(0)])),
            ],
            options={
                'db_table': 'fuel_element_type',
            },
        ),
        migrations.CreateModel(
            name='FuelPelletType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('time_inserted', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True)),
                ('outer_diameter', models.DecimalField(help_text='unit:cm', max_digits=7, decimal_places=3, validators=[django.core.validators.MinValueValidator(0)])),
                ('inner_diameter', models.DecimalField(help_text='unit:cm can be none when hollow', max_digits=7, decimal_places=3, validators=[django.core.validators.MinValueValidator(0)], null=True, blank=True)),
                ('height', models.DecimalField(help_text='unit:cm', max_digits=7, decimal_places=3, validators=[django.core.validators.MinValueValidator(0)])),
                ('dish_volume_percentage', models.DecimalField(help_text='unit:%', max_digits=9, decimal_places=6, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)])),
                ('dish_height', models.DecimalField(help_text='unit:cm', max_digits=7, decimal_places=3, validators=[django.core.validators.MinValueValidator(0)])),
                ('dish_diameter', models.DecimalField(help_text='unit:cm', max_digits=7, decimal_places=3, validators=[django.core.validators.MinValueValidator(0)])),
                ('roughness', models.DecimalField(help_text='unit:cm', max_digits=7, decimal_places=6, validators=[django.core.validators.MinValueValidator(0)], null=True, blank=True)),
                ('density_percentage', models.DecimalField(help_text='unit:%', max_digits=9, decimal_places=6, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)])),
                ('uncertainty_percentage', models.DecimalField(help_text='unit:%', max_digits=9, decimal_places=6, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)])),
                ('coating_thickness', models.DecimalField(help_text='unit:cm', max_digits=7, decimal_places=3, validators=[django.core.validators.MinValueValidator(0)])),
            ],
            options={
                'db_table': 'fuel_pellet_type',
            },
        ),
        migrations.CreateModel(
            name='Grid',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('time_inserted', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True)),
                ('model', models.CharField(max_length=40)),
                ('sleeve_weight', models.DecimalField(help_text='g', max_digits=15, decimal_places=5, validators=[django.core.validators.MinValueValidator(0)])),
                ('sleeve_thickness', models.DecimalField(help_text='cm', max_digits=10, decimal_places=5, validators=[django.core.validators.MinValueValidator(0)])),
                ('spring_weight', models.DecimalField(help_text='g', max_digits=15, decimal_places=5, validators=[django.core.validators.MinValueValidator(0)])),
                ('spring_thickness', models.DecimalField(help_text='cm', max_digits=10, decimal_places=5, validators=[django.core.validators.MinValueValidator(0)])),
                ('functionality', models.CharField(default='fix', max_length=5, choices=[('blend', 'blend'), ('fix', 'fix')])),
            ],
            options={
                'db_table': 'grid',
            },
        ),
        migrations.CreateModel(
            name='GridPosition',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('time_inserted', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True)),
                ('height', models.DecimalField(help_text='unit:cm', max_digits=7, decimal_places=3, validators=[django.core.validators.MinValueValidator(0)])),
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
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('time_inserted', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True)),
                ('upper_outer_diameter', models.DecimalField(help_text='unit:cm', max_digits=7, decimal_places=3, validators=[django.core.validators.MinValueValidator(0)])),
                ('upper_inner_diameter', models.DecimalField(help_text='unit:cm', max_digits=7, decimal_places=3, validators=[django.core.validators.MinValueValidator(0)])),
                ('buffer_outer_diameter', models.DecimalField(help_text='unit:cm', null=True, decimal_places=3, validators=[django.core.validators.MinValueValidator(0)], max_digits=7)),
                ('buffer_inner_diameter', models.DecimalField(help_text='unit:cm', null=True, decimal_places=3, validators=[django.core.validators.MinValueValidator(0)], max_digits=7)),
            ],
            options={
                'db_table': 'guid_tube',
            },
        ),
        migrations.CreateModel(
            name='GuidTubeMap',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('time_inserted', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True)),
                ('fuel_assembly_position', models.ForeignKey(to='Tragopan.FuelAssemblyPosition')),
                ('guid_tube', models.ForeignKey(to='Tragopan.GuidTube')),
            ],
            options={
                'db_table': 'guid_tube_map',
            },
        ),
        migrations.CreateModel(
            name='InstrumentTube',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('time_inserted', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True)),
                ('outer_diameter', models.DecimalField(help_text='unit:cm', max_digits=7, decimal_places=3, validators=[django.core.validators.MinValueValidator(0)])),
                ('inner_diameter', models.DecimalField(help_text='unit:cm', max_digits=7, decimal_places=3, validators=[django.core.validators.MinValueValidator(0)])),
            ],
            options={
                'db_table': 'instrument_tube',
            },
        ),
        migrations.CreateModel(
            name='InstrumentTubePosition',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('time_inserted', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True)),
                ('fuel_assembly_position', models.ForeignKey(to='Tragopan.FuelAssemblyPosition')),
                ('guid_tube', models.ForeignKey(to='Tragopan.InstrumentTube')),
            ],
            options={
                'db_table': 'instrument_tube_position',
            },
        ),
        migrations.CreateModel(
            name='LowerCap',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('time_inserted', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True)),
                ('height', models.DecimalField(help_text='unit:cm', max_digits=7, decimal_places=3, validators=[django.core.validators.MinValueValidator(0)])),
                ('weight', models.DecimalField(help_text='unit:cm', max_digits=7, decimal_places=3, validators=[django.core.validators.MinValueValidator(0)])),
                ('fuel_element_type', models.OneToOneField(to='Tragopan.FuelElementType')),
            ],
            options={
                'db_table': 'lower_cap',
            },
        ),
        migrations.CreateModel(
            name='LowerNozzle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('time_inserted', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True)),
                ('pitch', models.DecimalField(help_text='unit:cm', max_digits=7, decimal_places=3, validators=[django.core.validators.MinValueValidator(0)])),
                ('plate_thickness', models.DecimalField(help_text='unit:cm', max_digits=7, decimal_places=3, validators=[django.core.validators.MinValueValidator(0)])),
                ('plate_porosity', models.DecimalField(help_text='unit:%', max_digits=9, decimal_places=6, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)])),
                ('height', models.DecimalField(help_text='unit:cm', max_digits=7, decimal_places=3, validators=[django.core.validators.MinValueValidator(0)])),
                ('weight', models.DecimalField(help_text='unit:cm', max_digits=7, decimal_places=3, validators=[django.core.validators.MinValueValidator(0)])),
                ('fuel_assembly_model', models.OneToOneField(to='Tragopan.FuelAssemblyModel')),
            ],
            options={
                'db_table': 'lower_nozzle',
            },
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('time_inserted', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True)),
                ('nameCH', models.CharField(max_length=40)),
                ('nameEN', models.CharField(max_length=40)),
            ],
            options={
                'db_table': 'Material',
            },
        ),
        migrations.CreateModel(
            name='MaterialAttribute',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('time_inserted', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True)),
                ('density', models.DecimalField(help_text='unit:g/cm3', max_digits=15, decimal_places=5)),
                ('heat_capacity', models.DecimalField(help_text='J/kg*K', null=True, blank=True, decimal_places=5, max_digits=15)),
                ('thermal_conductivity', models.DecimalField(help_text='W/m*K', null=True, blank=True, decimal_places=5, max_digits=15)),
                ('expansion_coefficient', models.DecimalField(help_text='m/K', null=True, blank=True, decimal_places=5, max_digits=15)),
                ('code', models.CharField(blank=True, max_length=10)),
                ('material', models.OneToOneField(to='Tragopan.Material', related_name='attribute')),
            ],
            options={
                'db_table': 'material_attribute',
            },
        ),
        migrations.CreateModel(
            name='MaterialComposition',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('time_inserted', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True)),
                ('weight_percent', models.DecimalField(help_text='unit:%', max_digits=9, decimal_places=6, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)])),
                ('element', models.ForeignKey(to='Tragopan.Element', to_field='symbol')),
                ('material', models.ForeignKey(related_query_name='element', related_name='elements', to='Tragopan.Material')),
            ],
            options={
                'db_table': 'material_composition',
                'ordering': ['material'],
            },
        ),
        migrations.CreateModel(
            name='MaterialNuclide',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('time_inserted', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True)),
                ('weight_percent', models.DecimalField(help_text='unit:%', max_digits=9, decimal_places=6, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)])),
                ('material', models.ForeignKey(related_query_name='nuclide', related_name='nuclides', to='Tragopan.Material')),
            ],
            options={
                'db_table': 'material_nuclide',
            },
        ),
        migrations.CreateModel(
            name='Nuclide',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('time_inserted', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True)),
                ('atom_mass', models.DecimalField(max_digits=9, decimal_places=6, validators=[django.core.validators.MinValueValidator(0)])),
                ('abundance', models.DecimalField(help_text='unit:%', max_digits=9, decimal_places=6, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)])),
                ('reference', models.CharField(default='IUPAC', max_length=80)),
                ('element', models.ForeignKey(related_query_name='nuclide', related_name='nuclides', to_field='symbol', to='Tragopan.Element')),
            ],
            options={
                'db_table': 'Nuclide',
                'ordering': ['element'],
            },
        ),
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
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
            name='PlenumSpring',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('time_inserted', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True)),
                ('weight', models.DecimalField(help_text='unit:g', max_digits=10, decimal_places=3, validators=[django.core.validators.MinValueValidator(0)])),
                ('outer_diameter', models.DecimalField(help_text='unit:cm', max_digits=7, decimal_places=5, validators=[django.core.validators.MinValueValidator(0)])),
                ('wire_diameter', models.DecimalField(help_text='unit:cm', max_digits=7, decimal_places=5, validators=[django.core.validators.MinValueValidator(0)])),
                ('fuel_element_type', models.OneToOneField(to='Tragopan.FuelElementType')),
                ('material', models.ForeignKey(to='Tragopan.Material')),
            ],
            options={
                'db_table': 'plenum_spring',
            },
        ),
        migrations.CreateModel(
            name='PressureVessel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('time_inserted', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True)),
                ('outer_diameter', models.DecimalField(help_text='unit:cm', max_digits=7, decimal_places=3, validators=[django.core.validators.MinValueValidator(0)])),
                ('inner_diameter', models.DecimalField(help_text='unit:cm', max_digits=7, decimal_places=3, validators=[django.core.validators.MinValueValidator(0)])),
                ('weld_thickness', models.DecimalField(help_text='unit:cm', max_digits=7, decimal_places=3, validators=[django.core.validators.MinValueValidator(0)])),
                ('base_material', models.ForeignKey(to='Tragopan.Material', related_name='pressure_vessel_base')),
            ],
            options={
                'db_table': 'pressure_vessel',
            },
        ),
        migrations.CreateModel(
            name='PressureVesselInsulation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('time_inserted', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True)),
                ('outer_diameter', models.DecimalField(help_text='unit:cm', max_digits=7, decimal_places=3, validators=[django.core.validators.MinValueValidator(0)])),
                ('inner_diameter', models.DecimalField(help_text='unit:cm', max_digits=7, decimal_places=3, validators=[django.core.validators.MinValueValidator(0)])),
                ('material', models.ForeignKey(to='Tragopan.Material')),
            ],
            options={
                'db_table': 'pressure_vessel_insulation',
            },
        ),
        migrations.CreateModel(
            name='ReactorModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('time_inserted', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True)),
                ('model', models.CharField(max_length=50, choices=[('QNPC2', 'QNPC2'), ('QNPC1', 'QNPC1'), ('M310', 'M310'), ('CAP1000', 'CAP1000'), ('AP1000', 'AP1000')])),
                ('generation', models.CharField(max_length=2, choices=[('2', '2'), ('2+', '2+'), ('3', '3')])),
                ('reactor_type', models.CharField(max_length=3, choices=[('PWR', 'PWR'), ('BWR', 'BWR')])),
                ('geometry_type', models.CharField(max_length=9, choices=[('Cartesian', 'Cartesian'), ('Hexagonal', 'Hexagonal')])),
                ('row_symbol', models.CharField(max_length=6, choices=[('Number', 'Number'), ('Letter', 'Letter')])),
                ('column_symbol', models.CharField(max_length=6, choices=[('Number', 'Number'), ('Letter', 'Letter')])),
                ('num_loops', models.PositiveSmallIntegerField()),
                ('num_control_rod_mechanisms', models.PositiveSmallIntegerField()),
                ('core_equivalent_diameter', models.DecimalField(help_text='unit:cm', max_digits=7, decimal_places=3, validators=[django.core.validators.MinValueValidator(0)])),
                ('active_height', models.DecimalField(help_text='unit:cm', max_digits=7, decimal_places=3, validators=[django.core.validators.MinValueValidator(0)])),
                ('cold_state_assembly_pitch', models.DecimalField(help_text='unit:cm', max_digits=7, decimal_places=4, validators=[django.core.validators.MinValueValidator(0)])),
                ('hot_state_assembly_pitch', models.DecimalField(help_text='unit:cm', max_digits=7, decimal_places=4, validators=[django.core.validators.MinValueValidator(0)])),
            ],
            options={
                'db_table': 'reactor_model',
            },
        ),
        migrations.CreateModel(
            name='ReactorPosition',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('time_inserted', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True)),
                ('row', models.PositiveSmallIntegerField()),
                ('column', models.PositiveSmallIntegerField()),
                ('reactor_model', models.ForeignKey(related_query_name='position', related_name='positions', to='Tragopan.ReactorModel')),
            ],
            options={
                'db_table': 'reactor_position',
            },
        ),
        migrations.CreateModel(
            name='RipPlate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('time_inserted', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True)),
                ('height', models.DecimalField(help_text='unit:cm', max_digits=7, decimal_places=3, validators=[django.core.validators.MinValueValidator(0)])),
                ('thickness', models.DecimalField(help_text='unit:cm', max_digits=7, decimal_places=3, validators=[django.core.validators.MinValueValidator(0)])),
                ('width', models.DecimalField(help_text='unit:cm', max_digits=7, decimal_places=3, validators=[django.core.validators.MinValueValidator(0)], null=True, blank=True)),
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
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('time_inserted', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True)),
                ('height', models.DecimalField(help_text='unit:cm', max_digits=7, decimal_places=3, validators=[django.core.validators.MinValueValidator(0)])),
                ('outer_diameter', models.DecimalField(help_text='unit:cm', max_digits=7, decimal_places=3, validators=[django.core.validators.MinValueValidator(0)])),
                ('inner_diameter', models.DecimalField(help_text='unit:cm', max_digits=7, decimal_places=3, validators=[django.core.validators.MinValueValidator(0)])),
                ('angle', models.DecimalField(help_text='unit:degree', max_digits=7, decimal_places=3, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(360)])),
                ('loc_height', models.DecimalField(help_text='unit:cm', max_digits=7, decimal_places=3, validators=[django.core.validators.MinValueValidator(0)])),
                ('loc_theta', models.DecimalField(help_text='unit:degree', max_digits=7, decimal_places=3, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(360)])),
                ('gap_to_barrel', models.DecimalField(help_text='unit:cm', max_digits=7, decimal_places=3, validators=[django.core.validators.MinValueValidator(0)])),
                ('material', models.ForeignKey(to='Tragopan.Material')),
                ('reactor_model', models.ForeignKey(to='Tragopan.ReactorModel')),
            ],
            options={
                'db_table': 'thermal_shield',
            },
        ),
        migrations.CreateModel(
            name='UnitParameter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('time_inserted', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True)),
                ('unit', models.PositiveSmallIntegerField()),
                ('electric_power', models.DecimalField(help_text='unit:MW', max_digits=10, decimal_places=3, validators=[django.core.validators.MinValueValidator(0)])),
                ('thermal_power', models.DecimalField(help_text='unit:MW', max_digits=10, decimal_places=3, validators=[django.core.validators.MinValueValidator(0)])),
                ('heat_fraction_in_fuel', models.DecimalField(help_text='unit:%', max_digits=9, decimal_places=6, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)])),
                ('primary_system_pressure', models.DecimalField(help_text='unit:MPa', max_digits=15, decimal_places=5, validators=[django.core.validators.MinValueValidator(0)])),
                ('ave_linear_power_density', models.DecimalField(help_text='unit:KW/m', max_digits=15, decimal_places=5, validators=[django.core.validators.MinValueValidator(0)])),
                ('ave_vol_power_density', models.DecimalField(help_text='unit:KW/L', max_digits=15, decimal_places=5, validators=[django.core.validators.MinValueValidator(0)])),
                ('ave_mass_power_density', models.DecimalField(help_text='unit:KW/Kg (fuel)', max_digits=15, decimal_places=5, validators=[django.core.validators.MinValueValidator(0)])),
                ('best_estimated_cool_vol_flow_rate', models.DecimalField(help_text='unit:m3/h', max_digits=15, decimal_places=5, validators=[django.core.validators.MinValueValidator(0)])),
                ('bypass_flow_fraction', models.DecimalField(help_text='unit:%', max_digits=9, decimal_places=6, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)])),
                ('cold_state_cool_temp', models.DecimalField(help_text='unit:K', max_digits=15, decimal_places=5, validators=[django.core.validators.MinValueValidator(0)])),
                ('HZP_cool_inlet_temp', models.DecimalField(help_text='unit:K', max_digits=15, decimal_places=5, validators=[django.core.validators.MinValueValidator(0)])),
                ('HFP_cool_inlet_temp', models.DecimalField(help_text='unit:K', max_digits=15, decimal_places=5, validators=[django.core.validators.MinValueValidator(0)])),
                ('HFP_core_ave_cool_temp', models.DecimalField(help_text='unit:K', max_digits=15, decimal_places=5, validators=[django.core.validators.MinValueValidator(0)])),
                ('mid_power_cool_inlet_temp', models.DecimalField(help_text='unit:K', max_digits=15, decimal_places=5, validators=[django.core.validators.MinValueValidator(0)], null=True, blank=True)),
                ('plant', models.ForeignKey(to='Tragopan.Plant')),
                ('reactor_model', models.ForeignKey(to='Tragopan.ReactorModel')),
            ],
            options={
                'db_table': 'unit_parameter',
            },
        ),
        migrations.CreateModel(
            name='UpperCap',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('time_inserted', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True)),
                ('height', models.DecimalField(help_text='unit:cm', max_digits=7, decimal_places=3, validators=[django.core.validators.MinValueValidator(0)])),
                ('weight', models.DecimalField(help_text='unit:cm', max_digits=7, decimal_places=3, validators=[django.core.validators.MinValueValidator(0)])),
                ('fuel_element_type', models.OneToOneField(to='Tragopan.FuelElementType')),
                ('material', models.ForeignKey(to='Tragopan.Material')),
            ],
            options={
                'db_table': 'upper_cap',
            },
        ),
        migrations.CreateModel(
            name='UpperNozzle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('time_inserted', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True)),
                ('pitch', models.DecimalField(help_text='unit:cm', max_digits=7, decimal_places=3, validators=[django.core.validators.MinValueValidator(0)])),
                ('plate_thickness', models.DecimalField(help_text='unit:cm', max_digits=7, decimal_places=3, validators=[django.core.validators.MinValueValidator(0)])),
                ('plate_porosity', models.DecimalField(help_text='unit:%', max_digits=9, decimal_places=6, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)])),
                ('height', models.DecimalField(help_text='unit:cm', max_digits=7, decimal_places=3, validators=[django.core.validators.MinValueValidator(0)])),
                ('weight', models.DecimalField(help_text='unit:cm', max_digits=7, decimal_places=3, validators=[django.core.validators.MinValueValidator(0)])),
                ('fuel_assembly_model', models.OneToOneField(to='Tragopan.FuelAssemblyModel')),
                ('material', models.ForeignKey(to='Tragopan.Material')),
            ],
            options={
                'db_table': 'upper_nozzle',
            },
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('time_inserted', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True)),
                ('nameCH', models.CharField(max_length=40)),
                ('abbrCH', models.CharField(max_length=40)),
                ('nameEN', models.CharField(max_length=40)),
                ('abbrEN', models.CharField(max_length=40)),
                ('type', models.CharField(default='Designer', max_length=12, choices=[('Designer', 'Designer'), ('Manufacturer', 'Manufacturer'), ('Material', 'Material')])),
            ],
            options={
                'db_table': 'vendor',
            },
        ),
        migrations.AddField(
            model_name='uppernozzle',
            name='vendor',
            field=models.ForeignKey(to='Tragopan.Vendor'),
        ),
        migrations.AddField(
            model_name='uppercap',
            name='vendor',
            field=models.ForeignKey(to='Tragopan.Vendor'),
        ),
        migrations.AddField(
            model_name='thermalshield',
            name='vendor',
            field=models.ForeignKey(to='Tragopan.Vendor'),
        ),
        migrations.AddField(
            model_name='reactormodel',
            name='incore_instrument_position',
            field=models.ManyToManyField(blank=True, to='Tragopan.ReactorPosition', related_name='incore_instrument_position', db_table='incore_instrument_map'),
        ),
        migrations.AddField(
            model_name='reactormodel',
            name='thermal_couple_position',
            field=models.ManyToManyField(blank=True, to='Tragopan.ReactorPosition', related_name='thermal_couple_position', db_table='thermal_couple_map'),
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
            model_name='plenumspring',
            name='vendor',
            field=models.ForeignKey(to='Tragopan.Vendor'),
        ),
        migrations.AddField(
            model_name='materialnuclide',
            name='nuclide',
            field=models.ForeignKey(to='Tragopan.Nuclide'),
        ),
        migrations.AddField(
            model_name='material',
            name='material_composition',
            field=models.ManyToManyField(to='Tragopan.Element', through='Tragopan.MaterialComposition'),
        ),
        migrations.AddField(
            model_name='lowernozzle',
            name='material',
            field=models.ForeignKey(to='Tragopan.Material'),
        ),
        migrations.AddField(
            model_name='lowernozzle',
            name='vendor',
            field=models.ForeignKey(to='Tragopan.Vendor'),
        ),
        migrations.AddField(
            model_name='lowercap',
            name='material',
            field=models.ForeignKey(to='Tragopan.Material'),
        ),
        migrations.AddField(
            model_name='lowercap',
            name='vendor',
            field=models.ForeignKey(to='Tragopan.Vendor'),
        ),
        migrations.AddField(
            model_name='instrumenttube',
            name='material',
            field=models.ForeignKey(to='Tragopan.Material'),
        ),
        migrations.AddField(
            model_name='instrumenttube',
            name='vendor',
            field=models.ForeignKey(to='Tragopan.Vendor'),
        ),
        migrations.AddField(
            model_name='guidtube',
            name='material',
            field=models.ForeignKey(to='Tragopan.Material'),
        ),
        migrations.AddField(
            model_name='guidtube',
            name='vendor',
            field=models.ForeignKey(to='Tragopan.Vendor'),
        ),
        migrations.AddField(
            model_name='grid',
            name='sleeve_material',
            field=models.ForeignKey(related_query_name='grid_sleeve', related_name='grid_sleeves', to='Tragopan.Material'),
        ),
        migrations.AddField(
            model_name='grid',
            name='spring_material',
            field=models.ForeignKey(related_query_name='grid_spring', related_name='grid_springs', to='Tragopan.Material'),
        ),
        migrations.AddField(
            model_name='grid',
            name='vendor',
            field=models.ForeignKey(to='Tragopan.Vendor'),
        ),
        migrations.AddField(
            model_name='fuelpellettype',
            name='coating_material',
            field=models.ForeignKey(to='Tragopan.Material', related_name='fuel_pellet_coating'),
        ),
        migrations.AddField(
            model_name='fuelpellettype',
            name='material',
            field=models.ForeignKey(to='Tragopan.Material', related_name='fuel_pellet_material'),
        ),
        migrations.AddField(
            model_name='fuelelementtype',
            name='filling_gas_materia',
            field=models.ForeignKey(to='Tragopan.Material'),
        ),
        migrations.AddField(
            model_name='fuelelementtype',
            name='fuel_pellet',
            field=models.ManyToManyField(to='Tragopan.FuelPelletType', through='Tragopan.FuelElementPelletLoadingScheme'),
        ),
        migrations.AddField(
            model_name='fuelelementtype',
            name='vendor',
            field=models.ForeignKey(to='Tragopan.Vendor'),
        ),
        migrations.AddField(
            model_name='fuelelementpelletloadingscheme',
            name='fuel_element_type',
            field=models.ForeignKey(to='Tragopan.FuelElementType'),
        ),
        migrations.AddField(
            model_name='fuelelementpelletloadingscheme',
            name='fuel_pellet_type',
            field=models.ForeignKey(to='Tragopan.FuelPelletType'),
        ),
        migrations.AddField(
            model_name='fuelelementmap',
            name='fuel_element_type',
            field=models.ForeignKey(to='Tragopan.FuelElementType'),
        ),
        migrations.AddField(
            model_name='fuelassemblyrepository',
            name='plant',
            field=models.ForeignKey(to='Tragopan.Plant'),
        ),
        migrations.AddField(
            model_name='fuelassemblyrepository',
            name='vendor',
            field=models.ForeignKey(to='Tragopan.Vendor'),
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
        migrations.AddField(
            model_name='fakefuelelementtype',
            name='material',
            field=models.ForeignKey(to='Tragopan.Material'),
        ),
        migrations.AddField(
            model_name='fakefuelelementtype',
            name='vendor',
            field=models.ForeignKey(to='Tragopan.Vendor'),
        ),
        migrations.AddField(
            model_name='cycle',
            name='unit',
            field=models.ForeignKey(to='Tragopan.UnitParameter'),
        ),
        migrations.AddField(
            model_name='coreupperplate',
            name='material',
            field=models.ForeignKey(to='Tragopan.Material'),
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
            name='material',
            field=models.ForeignKey(to='Tragopan.Material'),
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
            name='material',
            field=models.ForeignKey(to='Tragopan.Material'),
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
            name='material',
            field=models.ForeignKey(to='Tragopan.Material'),
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
        migrations.AddField(
            model_name='claddingtube',
            name='fuel_element_type',
            field=models.OneToOneField(to='Tragopan.FuelElementType'),
        ),
        migrations.AddField(
            model_name='claddingtube',
            name='material',
            field=models.ForeignKey(to='Tragopan.Material'),
        ),
        migrations.AddField(
            model_name='claddingtube',
            name='vendor',
            field=models.ForeignKey(to='Tragopan.Vendor'),
        ),
        migrations.AlterUniqueTogether(
            name='unitparameter',
            unique_together=set([('plant', 'unit')]),
        ),
        migrations.AlterUniqueTogether(
            name='reactorposition',
            unique_together=set([('reactor_model', 'row', 'column')]),
        ),
        migrations.AlterUniqueTogether(
            name='nuclide',
            unique_together=set([('element', 'atom_mass')]),
        ),
        migrations.AlterOrderWithRespectTo(
            name='nuclide',
            order_with_respect_to='element',
        ),
        migrations.AlterUniqueTogether(
            name='materialcomposition',
            unique_together=set([('material', 'element')]),
        ),
        migrations.AlterOrderWithRespectTo(
            name='materialcomposition',
            order_with_respect_to='material',
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
