# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-10 19:14
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InspectionResults',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inspection_type', models.CharField(default='', max_length=200)),
                ('inspection_date', models.DateField(default=datetime.datetime(2017, 1, 10, 19, 14, 15, 906670, tzinfo=utc))),
                ('grade', models.CharField(default='', max_length=200)),
                ('score', models.IntegerField(default=0)),
                ('grade_date', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('camis', models.IntegerField(default=1, unique=True)),
                ('name', models.CharField(default='Restaurant', max_length=50)),
                ('boro', models.CharField(default='Manhattan', max_length=20)),
                ('building', models.CharField(default='0', max_length=10)),
                ('street', models.CharField(default='Main St', max_length=20)),
                ('zipcode', models.IntegerField(default=0)),
                ('phone', models.IntegerField(default=0)),
                ('cuisine', models.CharField(default='American', max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='inspectionresults',
            name='restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inspection.Restaurant'),
        ),
    ]