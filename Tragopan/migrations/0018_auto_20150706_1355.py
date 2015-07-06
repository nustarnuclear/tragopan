# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('Tragopan', '0017_auto_20150706_1342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reactormodel',
            name='cold_state_assembly_pitch',
            field=models.DecimalField(validators=[django.core.validators.MinValueValidator(0)], max_digits=7, help_text='unit:cm', decimal_places=4),
        ),
        migrations.AlterField(
            model_name='reactormodel',
            name='hot_state_assembly_pitch',
            field=models.DecimalField(validators=[django.core.validators.MinValueValidator(0)], max_digits=7, help_text='unit:cm', decimal_places=4),
        ),
    ]
