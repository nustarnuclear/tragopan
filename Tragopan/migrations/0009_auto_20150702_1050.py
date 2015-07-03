# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('Tragopan', '0008_auto_20150701_1503'),
    ]

    operations = [
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
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
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_inserted', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True)),
                ('density', models.DecimalField(help_text='unit:g_per_cm3', max_digits=20, decimal_places=10)),
                ('heat_capacity', models.DecimalField(help_text='J_per_kg_per_K', max_digits=20, decimal_places=10)),
                ('thermal_conductivity', models.DecimalField(help_text='W_per_m_per_K', max_digits=20, decimal_places=10)),
                ('expansion_coefficient', models.DecimalField(help_text='m_per_K', max_digits=20, decimal_places=10)),
                ('code', models.CharField(max_length=10, blank=True)),
                ('material', models.OneToOneField(to='Tragopan.Material')),
            ],
            options={
                'db_table': 'MaterialAttribute',
            },
        ),
        migrations.CreateModel(
            name='MaterialComposition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_inserted', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True)),
                ('weight_percent', models.DecimalField(help_text='unit:percentage', max_digits=9, decimal_places=6, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)])),
                ('element', models.ForeignKey(to_field='symbol', to='Tragopan.Element')),
                ('material', models.ForeignKey(to='Tragopan.Material')),
            ],
            options={
                'db_table': 'MaterialComposition',
                'ordering': ['material'],
            },
        ),
        migrations.CreateModel(
            name='MaterialNuclide',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_inserted', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True)),
                ('weight_percent', models.DecimalField(help_text='unit:percentage', max_digits=9, decimal_places=6, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)])),
                ('material', models.ForeignKey(to='Tragopan.Material')),
                ('nuclide', models.ForeignKey(to='Tragopan.Nuclide')),
            ],
            options={
                'db_table': 'MaterialNuclide',
            },
        ),
        migrations.AddField(
            model_name='material',
            name='material_composition',
            field=models.ManyToManyField(through='Tragopan.MaterialComposition', to='Tragopan.Element'),
        ),
        migrations.AlterUniqueTogether(
            name='materialcomposition',
            unique_together=set([('material', 'element')]),
        ),
        migrations.AlterOrderWithRespectTo(
            name='materialcomposition',
            order_with_respect_to='material',
        ),
    ]
