# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Client', '0002_client_produits'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='date_inscription',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
