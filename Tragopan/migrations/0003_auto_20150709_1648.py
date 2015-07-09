# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('Tragopan', '0002_auto_20150709_1342'),
    ]

    operations = [
        migrations.CreateModel(
            name='BurnablePoisonAssembly',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('time_inserted', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True)),
            ],
            options={
                'db_table': 'burnable_poison_assembly',
            },
        ),
        migrations.CreateModel(
            name='BurnablePoisonAssemblyNozzlePlug',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('time_inserted', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True)),
                ('burnable_poison_assembly', models.ForeignKey(to='Tragopan.BurnablePoisonAssembly')),
                ('guid_tube_position', models.OneToOneField(to='Tragopan.GuidTubeMap')),
            ],
            options={
                'db_table': 'burnable_poison_assembly_nozzle_plug',
            },
        ),
        migrations.CreateModel(
            name='BurnablePoisonMaterial',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('time_inserted', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True)),
                ('radius', models.DecimalField(validators=[django.core.validators.MinValueValidator(0)], help_text='unit:cm', max_digits=7, decimal_places=3)),
            ],
            options={
                'db_table': 'burnable_poison_rod_material',
            },
        ),
        migrations.CreateModel(
            name='BurnablePoisonRod',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('time_inserted', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True)),
                ('length', models.DecimalField(validators=[django.core.validators.MinValueValidator(0)], help_text='unit:cm', max_digits=7, decimal_places=3)),
                ('radial_map', models.ManyToManyField(through='Tragopan.BurnablePoisonMaterial', related_name='burnable_poison_rod', to='Tragopan.Material')),
            ],
            options={
                'db_table': 'burnable_poison_rod',
            },
        ),
        migrations.CreateModel(
            name='BurnablePoisonRodMap',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('time_inserted', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True)),
                ('burnable_poison_assembly', models.ForeignKey(to='Tragopan.BurnablePoisonAssembly')),
                ('burnable_poison_rod', models.ForeignKey(to='Tragopan.BurnablePoisonRod')),
                ('guid_tube_position', models.OneToOneField(to='Tragopan.GuidTubeMap')),
            ],
            options={
                'db_table': 'burnable_poison_rod_map',
            },
        ),
        migrations.CreateModel(
            name='ControlRodAssembly',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('time_inserted', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True)),
                ('overall_length', models.DecimalField(validators=[django.core.validators.MinValueValidator(0)], help_text='unit:cm', max_digits=7, decimal_places=3)),
            ],
            options={
                'db_table': 'control_rod_assembly',
            },
        ),
        migrations.CreateModel(
            name='ControlRodMap',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('time_inserted', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True)),
                ('control_rod_assembly', models.ForeignKey(to='Tragopan.ControlRodAssembly')),
            ],
            options={
                'db_table': 'control_rod_map',
            },
        ),
        migrations.CreateModel(
            name='ControlRodType',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('time_inserted', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True)),
                ('absorb_length', models.DecimalField(validators=[django.core.validators.MinValueValidator(0)], help_text='unit:cm', max_digits=7, decimal_places=3)),
                ('absorb_diameter', models.DecimalField(validators=[django.core.validators.MinValueValidator(0)], help_text='unit:cm', max_digits=7, decimal_places=3)),
                ('cladding_inner_diameter', models.DecimalField(validators=[django.core.validators.MinValueValidator(0)], help_text='unit:cm', max_digits=7, decimal_places=3)),
                ('cladding_outer_diameter', models.DecimalField(validators=[django.core.validators.MinValueValidator(0)], help_text='unit:cm', max_digits=7, decimal_places=3)),
                ('absorb_material', models.ForeignKey(to='Tragopan.Material', related_name='control_rod_absorb')),
                ('cladding_material', models.ForeignKey(to='Tragopan.Material', related_name='control_rod_cladding')),
            ],
            options={
                'db_table': 'control_rod_type',
            },
        ),
        migrations.CreateModel(
            name='NozzlePlugAssembly',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('time_inserted', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True)),
                ('weight', models.DecimalField(validators=[django.core.validators.MinValueValidator(0)], help_text='unit:Kg', max_digits=7, decimal_places=3)),
            ],
            options={
                'db_table': 'nozzle_plug_assembly',
            },
        ),
        migrations.CreateModel(
            name='NozzlePlugRod',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('time_inserted', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True)),
                ('length', models.DecimalField(validators=[django.core.validators.MinValueValidator(0)], help_text='unit:cm', max_digits=7, decimal_places=3)),
                ('diameter', models.DecimalField(validators=[django.core.validators.MinValueValidator(0)], help_text='unit:cm', max_digits=7, decimal_places=3)),
                ('material', models.ForeignKey(to='Tragopan.Material')),
            ],
            options={
                'db_table': 'nozzle_plug_rod',
            },
        ),
        migrations.CreateModel(
            name='NozzlePlugRodMap',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('time_inserted', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True)),
                ('guid_tube_position', models.OneToOneField(to='Tragopan.GuidTubeMap')),
                ('nozzle_plug_assembly', models.ForeignKey(to='Tragopan.NozzlePlugAssembly')),
                ('nozzle_plug_rod', models.ForeignKey(to='Tragopan.NozzlePlugRod')),
            ],
            options={
                'db_table': 'nozzle_plug_rod_map',
            },
        ),
        migrations.CreateModel(
            name='SourceAssembly',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('time_inserted', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True)),
            ],
            options={
                'db_table': 'source_assembly',
            },
        ),
        migrations.CreateModel(
            name='SourceAssemblyBPRod',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('time_inserted', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True)),
                ('burnable_poison_rod', models.ForeignKey(to='Tragopan.BurnablePoisonRod')),
                ('guid_tube_position', models.OneToOneField(to='Tragopan.GuidTubeMap')),
                ('source_assembly', models.ForeignKey(to='Tragopan.SourceAssembly')),
            ],
            options={
                'db_table': 'source_bp_rod',
            },
        ),
        migrations.CreateModel(
            name='SourceAssemblyNozzlePlug',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('time_inserted', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True)),
                ('guid_tube_position', models.OneToOneField(to='Tragopan.GuidTubeMap')),
                ('nozzle_plug_rod', models.ForeignKey(to='Tragopan.NozzlePlugRod')),
                ('source_assembly', models.ForeignKey(to='Tragopan.SourceAssembly')),
            ],
            options={
                'db_table': 'source_assembly_nozzle_plug',
            },
        ),
        migrations.CreateModel(
            name='SourceRodMap',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('time_inserted', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True)),
                ('guid_tube_position', models.OneToOneField(to='Tragopan.GuidTubeMap')),
                ('source_assembly', models.ForeignKey(to='Tragopan.SourceAssembly')),
            ],
            options={
                'db_table': 'source_rod_map',
            },
        ),
        migrations.CreateModel(
            name='SourceRodType',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('time_inserted', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True)),
                ('type', models.CharField(max_length=9, choices=[('primary', 'primary'), ('secondary', 'secondary')])),
                ('overall_length', models.DecimalField(validators=[django.core.validators.MinValueValidator(0)], help_text='unit:cm', max_digits=7, decimal_places=3)),
                ('diameter', models.DecimalField(validators=[django.core.validators.MinValueValidator(0)], help_text='unit:cm', max_digits=7, decimal_places=3)),
                ('strength', models.DecimalField(validators=[django.core.validators.MinValueValidator(0)], max_digits=7, decimal_places=3)),
                ('material', models.ForeignKey(to='Tragopan.Material')),
            ],
            options={
                'db_table': 'source_rod_type',
            },
        ),
        migrations.AddField(
            model_name='sourcerodmap',
            name='source_rod',
            field=models.ForeignKey(to='Tragopan.SourceRodType'),
        ),
        migrations.AddField(
            model_name='sourceassembly',
            name='burnable_poison_map',
            field=models.ManyToManyField(through='Tragopan.SourceAssemblyBPRod', related_name='source_burnable_poison', to='Tragopan.GuidTubeMap'),
        ),
        migrations.AddField(
            model_name='sourceassembly',
            name='nozzle_plug_rod_map',
            field=models.ManyToManyField(through='Tragopan.SourceAssemblyNozzlePlug', related_name='source_nozzle_plug', to='Tragopan.GuidTubeMap'),
        ),
        migrations.AddField(
            model_name='sourceassembly',
            name='source_rod_map',
            field=models.ManyToManyField(through='Tragopan.SourceRodMap', related_name='source_rod', to='Tragopan.GuidTubeMap'),
        ),
        migrations.AddField(
            model_name='nozzleplugassembly',
            name='nozzle_plug_rod',
            field=models.ManyToManyField(through='Tragopan.NozzlePlugRodMap', to='Tragopan.NozzlePlugRod'),
        ),
        migrations.AddField(
            model_name='controlrodmap',
            name='control_rod_type',
            field=models.ForeignKey(to='Tragopan.ControlRodType'),
        ),
        migrations.AddField(
            model_name='controlrodmap',
            name='guid_tube_position',
            field=models.OneToOneField(to='Tragopan.GuidTubeMap'),
        ),
        migrations.AddField(
            model_name='controlrodassembly',
            name='control_rod_map',
            field=models.ManyToManyField(through='Tragopan.ControlRodMap', to='Tragopan.GuidTubeMap'),
        ),
        migrations.AddField(
            model_name='burnablepoisonmaterial',
            name='burnable_poison_rod',
            field=models.ForeignKey(to='Tragopan.BurnablePoisonRod'),
        ),
        migrations.AddField(
            model_name='burnablepoisonmaterial',
            name='material',
            field=models.ForeignKey(to='Tragopan.Material'),
        ),
        migrations.AddField(
            model_name='burnablepoisonassemblynozzleplug',
            name='nozzle_plug_rod',
            field=models.ForeignKey(to='Tragopan.NozzlePlugRod'),
        ),
        migrations.AddField(
            model_name='burnablepoisonassembly',
            name='burnable_poison_map',
            field=models.ManyToManyField(through='Tragopan.BurnablePoisonRodMap', related_name='bp_burnable_poison', to='Tragopan.GuidTubeMap'),
        ),
        migrations.AddField(
            model_name='burnablepoisonassembly',
            name='nozzle_plug_rod_map',
            field=models.ManyToManyField(through='Tragopan.BurnablePoisonAssemblyNozzlePlug', related_name='bp_nozzle_plug', to='Tragopan.GuidTubeMap'),
        ),
    ]
