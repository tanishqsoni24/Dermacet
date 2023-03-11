from django.urls import path, include  
from . import views 

urlpatterns = [
    path('login',views.login, name="shop"),
    path('signup',views.signup, name="shop"),
]