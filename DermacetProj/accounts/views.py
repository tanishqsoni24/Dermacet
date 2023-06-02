from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import login as auth_login
from django.http import HttpResponse, HttpResponseRedirect
from .models import Profile, Cart, CartItems, MyOrders
from base.emails import send_forgot_password_email
import uuid
from django.contrib.auth.decorators import user_passes_test
# from shop.models import Product, Coupen, CartItems, Cart

def login(request):
    if(request.method=="POST"):
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user_obj = User.objects.filter(username = username)
        print(user_obj) 
        if not user_obj.exists():
            messages.error(request, "Account doesn't exists")
            return redirect("/accounts/login")
        
        if not user_obj[0].profile.is_email_verified:
            messages.error(request, "Account Not Verified")
            return redirect("/accounts/login")

        user_obj = authenticate(username = username, password = password)
        if user_obj:
            auth_login(request, user_obj)
            return redirect("/shop")

        messages.warning(request, "Invalid Credentials")
        return redirect("/accounts/login")
    return render(request, "accounts/login.html")

def signup(request):
    if(request.method=="POST"):
        full_Name = request.POST.get('full_name')
        first_name, last_name = full_Name.split(' ', 1)
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user_obj = User.objects.filter(username = username)
        if user_obj.exists():
            messages.error(request, "Username already exists")
            return redirect("/accounts/signup")
        user_obj = User.objects.create_user(username=username, email=email, password=password, first_name=first_name, last_name=last_name)
        user_obj.set_password(password)

        user_obj.save()

        messages.success(request, "An Email has been sent to your registered mail id")
        return redirect("/accounts/signup")
    return render(request, "accounts/signup.html")

def activate_email(request, email_token):
    try:
        user = Profile.objects.get(email_token=email_token)
        user.is_email_verified = True
        user.save()
        return redirect("/")
    except Exception as e:
        return HttpResponse("Invalid Email Token")

def logout(request):
    auth_logout(request)
    messages.success(request, "Logged Out Successfully")
    return redirect("/accounts/login")
    
def forgot_password(request):
    if request.method == "POST":
        username = request.POST.get('username')
        user_obj = User.objects.filter(username = username).first()
        if not user_obj:
            messages.error(request, "Account doesn't exists")
            return redirect("/accounts/signup")
        else:
            email_token = str(uuid.uuid4())
            user_obj.profile.forgot_password_token = email_token
            user_obj.profile.save()
            send_forgot_password_email(user_obj.email, email_token)
            messages.success(request, "An Email has been sent to your registered mail id")
            return redirect("/accounts/forgot-password")
    return render(request, "accounts/forgot_password.html")

def change_password(request, forgot_password_token):
    if request.method == "POST":
        password = request.POST.get('password')
        user_obj = Profile.objects.filter(forgot_password_token = forgot_password_token).first()
        if not user_obj:
            messages.error(request, "Invalid Token")
            return redirect("/accounts/forgot-password")
        else:
            user_obj.user.set_password(password)
            user_obj.user.save()
            messages.success(request, "Password Changed Successfully")
            return redirect("/accounts/login")
    return render(request, "accounts/change_password.html")

def My_Orders(request):
    Paid_Cart = Cart.objects.filter(user=request.user, is_paid=True).order_by('-publish_date')
    Paid_Orders = MyOrders.objects.filter(cart__in=Paid_Cart)
    return render(request, "accounts/My_Orders.html", {'Paid_Orders':Paid_Orders})

@user_passes_test(lambda u: u.is_superuser)
def admin_all_orders(request):
    all_orders = MyOrders.objects.all()
    return render(request, "accounts/admin_all_orders.html", {'all_orders':all_orders})


def view_order(request, order_id):
    try:
        order = MyOrders.objects.filter(cart__razorpay_order_id=order_id).first()
        if order:
            cart_items = order.cart.cart_items.all()

            # Getting Cart total without Coupen

            cart_total_without_coupon = order.cart.get_cart_total_without_coupen(order_id)

            # Getting Minimum Amount of Coupon

            coupon = order.cart.coupen
            if coupon:
                minimum_amount = coupon.minimun_amount   
            else:
                minimum_amount = 0
            
            quantity = sum([cart_item.quantity if cart_item.quantity < cart_item.product.product_available_count else 0 for cart_item in cart_items])
            return render(request, "accounts/view_order.html", {'cart_items':cart_items, 'order':order, "quantity":quantity, 'minimum_amount':minimum_amount, 'cart_total_without_coupon': cart_total_without_coupon})
    except Exception as e:
        print(e)
        return HttpResponse("Invalid Order Id")