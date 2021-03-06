# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Societe',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nom', models.CharField(max_length=1024)),
                ('directeur', models.CharField(max_length=1024)),
                ('courriel', models.EmailField(max_length=254)),
                ('date_creation', models.DateTimeField()),
            ],
        ),
    ]
