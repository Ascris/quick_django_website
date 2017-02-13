# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Societe', '0001_initial'),
        ('Produit', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='produit',
            name='societes',
            field=models.ManyToManyField(to='Societe.Societe'),
        ),
    ]
