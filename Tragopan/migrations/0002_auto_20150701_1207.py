# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Tragopan', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='element',
            name='reference',
            field=models.CharField(default='IUPAC', max_length=80),
        ),
        migrations.AlterField(
            model_name='nuclide',
            name='reference',
            field=models.CharField(default='IUPAC', max_length=80),
        ),
    ]
