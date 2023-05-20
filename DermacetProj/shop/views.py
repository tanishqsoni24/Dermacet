from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Product, Category, Newsletter, Coupen
from django.contrib import messages
from accounts.models import Cart, CartItems
from django.contrib.auth.decorators import login_required
import razorpay
from django.conf import settings

# Create your views here.

def shop(request):
    Categories = Category.objects.all()
    products = Product.objects.all()
    # Searching
    if request.GET.get('category'):
        category_fetch = request.GET.get('category')
        if category_fetch == "ALL":
            return render(request, "shop/index.html", {'products':products,'category':Categories})
        category_obj = Category.objects.get(cat_name=category_fetch)
        products = Product.objects.filter(category=category_obj)
        return render(request, "shop/index.html", {'products':products,'category':Categories, 'checked_category':category_fetch})
    return render(request, "shop/index.html", {'products':products,'category':Categories})

def prodDescp(request,slug):
    try:
        product = Product.objects.get(slug=slug)
        return render(request, "shop/product_descp.html",{'prodDescp':product})

    except Exception as e:
        print(e)
        return HttpResponse("404 Not Foundss")

def manageNewsLetter(request):
    if request.method == "POST":    
        email = request.POST.get("email")
        newslettersave = Newsletter(email=email)
        newslettersave.save()
        request.session["alert"] = "Email Sent Successfully!"
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        return HttpResponse("500 FOUND")

def manageSearch(request):
    query = request.GET.get("query")
    all_prods_name = Product.objects.filter(prod_name__icontains = query)
    all_prods_descp = Product.objects.filter(prod_descp__icontains = query)
    searchResult = all_prods_name | all_prods_descp
    return render(request, "shop/index.html", {'products':searchResult, 'query':query})

def cart(request, uid):
    if(request.user.is_authenticated):        
        product = Product.objects.get(uid=uid)
        user = request.user
        cart, _ = Cart.objects.get_or_create(user=user, is_paid=False)
        cart_items = CartItems.objects.create(cart=cart, product=product)
        cart_items.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    messages.warning(request, "LogIn for adding your items to cart")
    return redirect("/accounts/login")


def cartView(request):
    if(request.user.is_authenticated):
        carts = Cart.objects.filter(is_paid = False, user = request.user)
        cart_items = []
        for cart in carts:
            cart_items.extend(list(cart.cart_items.all()))
        if request.method == 'POST':

            # Coupen

            coupen = request.POST.get("coupen")
            coupen_obj = Coupen.objects.filter(coupen_code__iexact=coupen)
            if not coupen_obj.exists():
                messages.warning(request, "Coupen does not exist")
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

            if carts.first().coupen is not None:
                messages.warning(request, "Coupen Already exist")
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

            if coupen_obj.first().minimun_amount > carts.first().get_cart_total():
                messages.warning(request, f"Amount Should be greater than {coupen_obj.first().minimun_amount}")
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

            if coupen_obj.first().is_expired:
                messages.warning(request, f"Coupen is Expired!")
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

            cart = carts.first()
            cart.coupen = coupen_obj.first()
            cart.save()
            messages.success(request, "Coupen Applied Successfully!")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        
        # Razorpay

        if carts:
            if not (carts.first().get_cart_total()*100) <= 0:
                client = razorpay.Client(auth=(settings.KEY, settings.SECRET))
                data = { "amount": carts.first().get_cart_total()*100, "currency": "INR", "payment_capture": 1 }
                payment = client.order.create(data=data)
                carts.first().set_razorpay_order_id(payment['id'])
                return render(request, 'shop/add_to_cart.html', {'cart_items': cart_items, 'payment':payment})
        return render(request, 'shop/add_to_cart.html', {'cart_items': cart_items})
    messages.warning(request, "LogIn First")
    return redirect('/accounts/login')

def success(request):
    if request.GET.get("order_ID",False) or Cart.objects.filter(razorpay_order_id=request.GET.get("order_ID",False)).first():
        carts = Cart.objects.filter(is_paid = False, user = request.user)
        order_id = request.GET.get('order_ID')
        amount = request.GET.get('amount')
        cart = Cart.objects.filter(razorpay_order_id=order_id).first()
        if cart:
            if carts:
                if carts.first().get_cart_total()*100 != int(amount):
                    return HttpResponse("Amount Mismatch")
            if not cart.is_paid:
                cart.is_paid = True
                cart.set_payment_done_amount(amount[0:-2])
                cart.save()
                return render(request, 'shop/payment_successful.html', {'order_id':order_id, 'amount':amount[0:-2]})
            return HttpResponse("Already Paid")
        return HttpResponse("Order ID Mismatch")
    return HttpResponse("404 Error")

def remove_cart(request, cart_item_uid):
    try:
        cart_item = CartItems.objects.get(uid=cart_item_uid)
        cart_item.delete()
    except Exception as e:
        print(e)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
