from django.contrib import admin
from products.models import Product,CatalogCategory

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}


class CatalogCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}

admin.site.register(Product,ProductAdmin)
admin.site.register(CatalogCategory,CatalogCategoryAdmin)
# Register your models here.
