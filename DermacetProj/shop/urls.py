from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.shop, name="shop"),
    path('add-to-cart/<uid>',views.cart, name="cart"),
    path('remove-cart/<cart_item_uid>',views.remove_cart, name="remove_cart"),
    path('remove-cart/<coupon_uid>/',views.remove_coupon, name="remove_coupon"),
    path('update_cart_quantity/<cart_item_uid>/',views.update_cart_quantity, name="update_cart_quantity"),
    path('cart/',views.cartView, name="cartView"),
    path('manageNewsLetter/', views.manageNewsLetter, name="manageNewsLetter"),
    path('success/', views.success, name="success"),
    path('delete_review/<uuid:review_id>/', views.delete_review, name="delete_review"),
    path('<slug>/',views.prodDescp, name="Product"),
]