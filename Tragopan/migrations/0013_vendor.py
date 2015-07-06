# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Tragopan', '0012_auto_20150703_1927'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('time_inserted', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True)),
                ('nameCH', models.CharField(max_length=40)),
                ('abbrCH', models.CharField(max_length=40)),
                ('nameEN', models.CharField(max_length=40)),
                ('abbrEN', models.CharField(max_length=40)),
            ],
            options={
                'db_table': 'vendor',
            },
        ),
    ]
