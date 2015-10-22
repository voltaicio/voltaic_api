# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0002_auto_20150830_2354'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='photo',
            options={'ordering': ['-created']},
        ),
    ]
