# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_cart_product'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cart',
            options={'ordering': ['date_added']},
        ),
        migrations.AlterModelTable(
            name='cart',
            table='cart_items',
        ),
    ]
