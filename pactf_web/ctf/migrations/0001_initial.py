# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-21 20:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('p_id', models.AutoField(primary_key=True, serialize=False)),
                ('points', models.IntegerField()),
                ('name', models.CharField(max_length=20, unique=True)),
                ('desc', models.TextField()),
                ('hint', models.TextField(default='')),
                ('grader', models.FilePathField(help_text='Path to the grading script')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('t_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('score', models.IntegerField()),
            ],
        ),
    ]
