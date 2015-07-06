# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Tragopan', '0018_auto_20150706_1355'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='reactorposition',
            unique_together=set([('reactor_model', 'row', 'column')]),
        ),
    ]
