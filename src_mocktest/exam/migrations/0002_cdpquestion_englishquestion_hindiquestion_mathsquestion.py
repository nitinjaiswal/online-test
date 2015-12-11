# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CdpQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('qid', models.IntegerField()),
                ('qEnglish', models.CharField(max_length=1000)),
                ('qHindi', models.CharField(max_length=1000)),
                ('qOption', models.CharField(max_length=100)),
                ('qAnswer', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='EnglishQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('qid', models.IntegerField()),
                ('qEnglish', models.CharField(max_length=1000)),
                ('qOption', models.CharField(max_length=100)),
                ('qAnswer', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='HindiQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('qid', models.IntegerField()),
                ('qHindi', models.CharField(max_length=1000)),
                ('qOption', models.CharField(max_length=100)),
                ('qAnswer', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='MathsQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('qid', models.IntegerField()),
                ('qEnglish', models.CharField(max_length=1000)),
                ('qHindi', models.CharField(max_length=1000)),
                ('qOption', models.CharField(max_length=100)),
                ('qAnswer', models.CharField(max_length=100)),
            ],
        ),
    ]
