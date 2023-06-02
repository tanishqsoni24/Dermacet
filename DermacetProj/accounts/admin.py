from django.contrib import admin
from .models import Profile, Cart, CartItems, MyOrders

# Register your models here.

class CartItemsInline(admin.StackedInline):
    model = CartItems

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    date_hierarchy = 'publish_date'
    inlines = [CartItemsInline]

admin.site.register((Profile, CartItems, MyOrders))
