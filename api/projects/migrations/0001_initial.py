# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('utils', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('abstractbase_ptr', models.OneToOneField(auto_created=True, serialize=False, parent_link=True, to='utils.AbstractBase', primary_key=True)),
                ('description', models.TextField(verbose_name='description')),
            ],
            options={
                'abstract': False,
            },
            bases=('utils.abstractbase',),
        ),
    ]
