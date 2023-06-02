from django.contrib import admin
from shop.models import *

# Register your models here.
admin.site.register((Category,Coupen, Newsletter, Reviews))

class ProductImageInline(admin.StackedInline):
    model = ProdImage

class ProductDescpInline(admin.StackedInline):
    model = Product_Description

class ProductReviewInline(admin.StackedInline):
    model = Reviews


@admin.register(Product)
class PostAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline, ProductDescpInline, ProductReviewInline]
