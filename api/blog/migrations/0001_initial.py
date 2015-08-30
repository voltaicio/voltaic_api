# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('utils', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('abstractbase_ptr', models.OneToOneField(auto_created=True, serialize=False, parent_link=True, to='utils.AbstractBase', primary_key=True)),
                ('body', models.TextField(verbose_name='body')),
            ],
            options={
                'abstract': False,
            },
            bases=('utils.abstractbase',),
        ),
    ]
