# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('taxonomy', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('is_active', models.BooleanField(verbose_name='is active', default=False)),
                ('created', model_utils.fields.AutoCreatedField(editable=False, verbose_name='created', default=django.utils.timezone.now)),
                ('modified', model_utils.fields.AutoLastModifiedField(editable=False, verbose_name='modified', default=django.utils.timezone.now)),
                ('slug', models.SlugField(unique=True, verbose_name='slug')),
                ('title', models.CharField(verbose_name='title', max_length=128)),
                ('description', models.TextField(verbose_name='description')),
                ('tags', models.ManyToManyField(verbose_name='tags', to='taxonomy.Tag', blank=True)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]
