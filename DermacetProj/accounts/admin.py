from django.contrib import admin
from .models import Profile, Cart, CartItems

# Register your models here.

class CartItemsInline(admin.StackedInline):
    model = CartItems

@admin.register(Cart)
class PostAdmin(admin.ModelAdmin):
    inlines = [CartItemsInline]

admin.site.register((Profile, CartItems))
