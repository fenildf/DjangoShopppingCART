from django.contrib import admin
from .models import Catalog

class CatalogAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}	



admin.site.register(Catalog,CatalogAdmin)

# Register your models here.
