# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Tragopan', '0011_auto_20150702_1253'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='materialattribute',
            table='material_attribute',
        ),
        migrations.AlterModelTable(
            name='materialcomposition',
            table='material_composition',
        ),
        migrations.AlterModelTable(
            name='materialnuclide',
            table='material_nuclide',
        ),
    ]
