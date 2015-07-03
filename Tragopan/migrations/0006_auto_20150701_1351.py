# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('Tragopan', '0005_auto_20150701_1255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nuclide',
            name='abundance',
            field=models.DecimalField(max_digits=8, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)], decimal_places=6, help_text='unit:percentage'),
        ),
    ]
