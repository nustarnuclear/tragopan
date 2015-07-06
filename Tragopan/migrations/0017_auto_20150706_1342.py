# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Tragopan', '0016_auto_20150706_1325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reactormodel',
            name='model',
            field=models.CharField(max_length=50, choices=[('QNPC2', 'QNPC2'), ('QNPC1', 'QNPC1'), ('M310', 'M310'), ('CAP1000', 'CAP1000'), ('AP1000', 'AP1000')]),
        ),
    ]
