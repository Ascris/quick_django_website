# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Produit', '0002_produit_societes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produit',
            name='date_creation',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
