from django.contrib import admin
from shop.models import *

# Register your models here.
admin.site.register(Category)

class ProductImageInline(admin.StackedInline):
    model = ProdImage


@admin.register(Product)
class PostAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]