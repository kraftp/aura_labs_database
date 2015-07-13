# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('labs_database', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lab',
            name='pi_name',
            field=models.CharField(max_length=200, verbose_name=b'PI Name'),
        ),
    ]
