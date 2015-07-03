# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Tragopan', '0003_auto_20150701_1213'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='element',
            options={'ordering': ['atomic_number']},
        ),
    ]
