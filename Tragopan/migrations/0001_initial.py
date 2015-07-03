# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Element',
            fields=[
                ('time_inserted', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True)),
                ('atomic_number', models.PositiveSmallIntegerField(serialize=False, primary_key=True)),
                ('symbol', models.CharField(max_length=8, unique=True)),
                ('nameCH', models.CharField(max_length=8)),
                ('nameEN', models.CharField(max_length=40)),
                ('reference', models.CharField(max_length=80, blank=True)),
            ],
            options={
                'db_table': 'element',
            },
        ),
        migrations.CreateModel(
            name='Nuclide',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('time_inserted', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True)),
                ('atom_mass', models.DecimalField(validators=[django.core.validators.MinValueValidator(0)], decimal_places=6, max_digits=9)),
                ('abundance', models.DecimalField(validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)], decimal_places=4, max_digits=6, help_text='unit:percentage')),
                ('reference', models.CharField(max_length=80, blank=True)),
                ('element', models.ForeignKey(related_query_name='nuclide', to_field='symbol', related_name='nuclides', to='Tragopan.Element')),
            ],
            options={
                'db_table': 'isotopic_composition',
            },
        ),
        migrations.AlterUniqueTogether(
            name='nuclide',
            unique_together=set([('element', 'atom_mass')]),
        ),
        migrations.AlterOrderWithRespectTo(
            name='nuclide',
            order_with_respect_to='element',
        ),
    ]
