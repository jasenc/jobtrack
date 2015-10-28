# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0003_applist'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='app_list',
            field=models.ForeignKey(default=None, to='applications.AppList'),
        ),
    ]
