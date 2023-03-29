from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.shop, name="shop"),
    path('<slug>',views.prodDescp, name="Product"),
    path('manageNewsLetter/', views.manageNewsLetter, name="manageNewsLetter"),
    path('manageSearch/', views.manageSearch, name="manageSearch"),
]