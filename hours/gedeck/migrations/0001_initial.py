# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('required', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'Activities',
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=200)),
                ('activities', models.ManyToManyField(to='gedeck.Activity')),
            ],
        ),
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254)),
                ('rsvp', models.BooleanField(default=False)),
                ('notify', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='GuestActivityRsvp',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('activity', models.ForeignKey(to='gedeck.Activity')),
                ('guest', models.ForeignKey(to='gedeck.Guest')),
            ],
        ),
        migrations.CreateModel(
            name='GuestPreference',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('preference', models.TextField()),
                ('event', models.ForeignKey(to='gedeck.Event')),
                ('guest', models.ForeignKey(to='gedeck.Guest')),
            ],
        ),
        migrations.CreateModel(
            name='GuestSelection',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('event', models.ForeignKey(to='gedeck.Event')),
                ('guest', models.ForeignKey(to='gedeck.Guest')),
            ],
        ),
        migrations.CreateModel(
            name='Invitation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('ref', models.CharField(max_length=100)),
                ('lead', models.TextField(null=True, blank=True)),
                ('lead_on_complete', models.TextField(null=True, blank=True)),
                ('event', models.ForeignKey(to='gedeck.Event')),
                ('guests', models.ManyToManyField(to='gedeck.Guest', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('active', models.BooleanField(default=True)),
                ('type', models.CharField(max_length=10, choices=[(b'APPETIZER', 'Appetizer'), (b'ENTREE', 'Entr\xe9e'), (b'DESSERT', 'Dessert')])),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('order', models.IntegerField(default=0)),
                ('menu', models.ForeignKey(to='gedeck.Menu')),
            ],
        ),
        migrations.CreateModel(
            name='Preference',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('active', models.BooleanField(default=True)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('required', models.BooleanField(default=True)),
            ],
        ),
        migrations.AddField(
            model_name='invitation',
            name='menu',
            field=models.ForeignKey(blank=True, to='gedeck.Menu', null=True),
        ),
        migrations.AddField(
            model_name='invitation',
            name='preference',
            field=models.ForeignKey(blank=True, to='gedeck.Preference', null=True),
        ),
        migrations.AddField(
            model_name='guestselection',
            name='items',
            field=models.ManyToManyField(to='gedeck.MenuItem', blank=True),
        ),
    ]
