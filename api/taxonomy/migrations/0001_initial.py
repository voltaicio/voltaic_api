# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('created', model_utils.fields.AutoCreatedField(editable=False, verbose_name='created', default=django.utils.timezone.now)),
                ('modified', model_utils.fields.AutoLastModifiedField(editable=False, verbose_name='modified', default=django.utils.timezone.now)),
                ('slug', models.SlugField(unique=True, verbose_name='slug')),
                ('title', models.CharField(verbose_name='title', max_length=128)),
                ('tags', models.ManyToManyField(verbose_name='tags', to='taxonomy.Tag', blank=True)),
            ],
            options={
                'ordering': ['title'],
            },
        ),
    ]
