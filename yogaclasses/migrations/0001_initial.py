# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-13 23:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Studio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sname', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tname', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='YogaClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('start_time', models.TimeField(blank=True, null=True)),
                ('end_time', models.TimeField(blank=True, null=True)),
                ('studio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yogaclasses.Studio')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yogaclasses.Teacher')),
            ],
        ),
    ]
