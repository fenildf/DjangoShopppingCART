# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_product'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Product',
        ),
    ]
