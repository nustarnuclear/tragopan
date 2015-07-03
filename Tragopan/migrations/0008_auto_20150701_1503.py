# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('Tragopan', '0007_auto_20150701_1357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nuclide',
            name='abundance',
            field=models.DecimalField(validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)], decimal_places=6, max_digits=9, help_text='unit:percentage'),
        ),
    ]
