# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_delete_product'),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CatalogCategory',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=300)),
                ('slug', models.SlugField(max_length=150)),
                ('description', models.TextField(blank=True)),
                ('catalog', models.ForeignKey(related_name='categories', to='catalog.Catalog')),
                ('parent', models.ForeignKey(related_name='children', null=True, to='products.CatalogCategory', blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(related_name='products', to='products.CatalogCategory', default=''),
            preserve_default=False,
        ),
    ]
