# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Tragopan', '0002_auto_20150701_1207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='element',
            name='atomic_number',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
