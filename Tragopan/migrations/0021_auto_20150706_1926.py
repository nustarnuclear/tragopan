# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Tragopan', '0020_auto_20150706_1624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reactorposition',
            name='reactor_model',
            field=models.ForeignKey(to='Tragopan.ReactorModel', related_query_name='position', related_name='positions'),
        ),
    ]
