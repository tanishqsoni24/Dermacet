from django.urls import path, include  
from . import views 

urlpatterns = [
    path('login',views.login, name="shop"),
    path('signup',views.signup, name="shop"),
    path('logout',views.logout, name="logout"),
    path('My_Orders/',views.My_Orders, name="My_Orders"),
    path('all_Orders/',views.admin_all_orders, name="admin_all_orders"),
    path('My_Orders/<order_id>/',views.view_order, name="view_order"),
    path('forgot-password/',views.forgot_password, name="forgot-password"),
    path('change-password/<forgot_password_token>/',views.change_password, name="change-password"),
    path('activate/<email_token>',views.activate_email, name="activate_email"),
]