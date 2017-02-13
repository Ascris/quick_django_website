# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Produit', '0001_initial'),
        ('Client', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='produits',
            field=models.ManyToManyField(to='Produit.Produit'),
        ),
    ]
