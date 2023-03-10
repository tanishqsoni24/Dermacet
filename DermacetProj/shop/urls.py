from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.shop, name="shop"),
    path('productDescp',views.prodDescp, name="shop"),
]