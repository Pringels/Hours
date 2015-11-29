# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'get_latest_by': 'post_date'},
        ),
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.CharField(default='test', max_length=256),
            preserve_default=False,
        ),
    ]
