from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.shop, name="shop"),
    path('add-to-cart/<uid>',views.cart, name="cart"),
    path('remove-cart/<cart_item_uid>',views.remove_cart, name="remove_cart"),
    path('cart/',views.cartView, name="cartView"),
    path('manageNewsLetter/', views.manageNewsLetter, name="manageNewsLetter"),
    path('success/', views.success, name="success"),
    path('manageSearch/', views.manageSearch, name="manageSearch"),
    path('<slug>/',views.prodDescp, name="Product"),
]