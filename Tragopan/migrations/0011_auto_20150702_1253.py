# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Tragopan', '0010_auto_20150702_1227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='materialattribute',
            name='material',
            field=models.OneToOneField(related_name='attribute', to='Tragopan.Material'),
        ),
        migrations.AlterField(
            model_name='materialcomposition',
            name='material',
            field=models.ForeignKey(related_name='elements', to='Tragopan.Material', related_query_name='element'),
        ),
        migrations.AlterField(
            model_name='materialnuclide',
            name='material',
            field=models.ForeignKey(related_name='nuclides', to='Tragopan.Material', related_query_name='nuclide'),
        ),
    ]
