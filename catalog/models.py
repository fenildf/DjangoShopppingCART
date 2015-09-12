from django.db import models
from datetime import datetime
from django.template.defaultfilters import slugify
class Catalog(models.Model):
    name=models.CharField(max_length=255)
    slug=models.SlugField(max_length=150)
    publisher=models.CharField(max_length=300)
    description=models.TextField()
    pub_date=models.DateTimeField(default=datetime.now)

    def save(self,*args,**kwargs):
	    self.slug=slugify(self.name)
	    super(Catalog,self).save(*args,**kwargs) 	

    def __str__(self):
        return self.name	

	
# Create your models here.
