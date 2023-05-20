from django.contrib import admin
from shop.models import *

# Register your models here.
admin.site.register((Category,Coupen, Newsletter))

class ProductImageInline(admin.StackedInline):
    model = ProdImage

class ProductDescpInline(admin.StackedInline):
    model = Product_Description


@admin.register(Product)
class PostAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline, ProductDescpInline]
