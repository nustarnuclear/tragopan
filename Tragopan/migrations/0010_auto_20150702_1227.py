# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Tragopan', '0009_auto_20150702_1050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='materialattribute',
            name='expansion_coefficient',
            field=models.DecimalField(null=True, decimal_places=10, help_text='m_per_K', blank=True, max_digits=20),
        ),
        migrations.AlterField(
            model_name='materialattribute',
            name='heat_capacity',
            field=models.DecimalField(null=True, decimal_places=10, help_text='J_per_kg_per_K', blank=True, max_digits=20),
        ),
        migrations.AlterField(
            model_name='materialattribute',
            name='thermal_conductivity',
            field=models.DecimalField(null=True, decimal_places=10, help_text='W_per_m_per_K', blank=True, max_digits=20),
        ),
    ]
