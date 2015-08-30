# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('utils', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('abstractbase_ptr', models.OneToOneField(auto_created=True, serialize=False, parent_link=True, to='utils.AbstractBase', primary_key=True)),
                ('description', models.TextField(verbose_name='description')),
                ('image', models.ImageField(verbose_name='image', upload_to='')),
            ],
            options={
                'abstract': False,
            },
            bases=('utils.abstractbase',),
        ),
    ]
