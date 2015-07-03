# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Tragopan', '0006_auto_20150701_1351'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='nuclide',
            options={'ordering': ['element']},
        ),
    ]
