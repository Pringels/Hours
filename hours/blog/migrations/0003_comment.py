# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20151129_1633'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('author', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=200)),
                ('comment', models.TextField()),
                ('pub_date', models.DateField()),
                ('post', models.ForeignKey(to='blog.Post')),
            ],
            options={
                'ordering': ('pub_date',),
            },
        ),
    ]
