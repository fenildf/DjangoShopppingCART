
from django.db import models
from django.template.defaultfilters import slugify
from django.db.models import permalink


class Product(models.Model):
    category=models.ForeignKey('CatalogCategory',related_name='products')
    name=models.CharField(max_length=300)
    description=models.TextField(max_length=150)
    photo=models.ImageField(upload_to='images',height_field=None,width_field=None,max_length=100)
    manufacturer=models.CharField(max_length=300,blank=True)
    price_in_dollars=models.DecimalField(max_digits=6,decimal_places=2)
    slug=models.SlugField(max_length=300)

    def save(self,*args,**kwargs):
            self.slug=slugify(self.name)
            super(Product,self).save(*args,**kwargs)

    def __str__(self):
        return self.name

    @permalink
    def get_absolute_url(self):
        return ('product',None,{'slug':self.slug})


class CatalogCategory(models.Model):
    catalog=models.ForeignKey('catalog.Catalog',related_name='categories')
    parent=models.ForeignKey('self',blank=True,null=True,related_name='children')
    name=models.CharField(max_length=300)
    slug=models.SlugField(max_length=150)
    description=models.TextField(blank=True)

    def save(self,*args,**kwargs):
            self.slug=slugify(self.name)
            super(CatalogCategory,self).save(*args,**kwargs)
            
    def __unicode__(self):
        if self.parent:
            return u'%s: %s - %s' % (self.catalog.name, self.parent.name, self.name)
            return u'%s: %s' % (self.catalog.name, self.name)
# Create your models here.
