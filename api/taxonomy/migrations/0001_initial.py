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
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('slug', models.SlugField(unique=True, verbose_name='slug')),
                ('title', models.CharField(max_length=128, verbose_name='title')),
                ('tags', models.ManyToManyField(blank=True, verbose_name='tags', to='taxonomy.Tag')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
    ]
