# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('qid', models.IntegerField()),
                ('qEnglish', models.CharField(max_length=1000)),
                ('qHindi', models.CharField(max_length=1000)),
                ('qOption', models.CharField(max_length=100)),
                ('qAnswer', models.CharField(max_length=10)),
            ],
        ),
    ]
