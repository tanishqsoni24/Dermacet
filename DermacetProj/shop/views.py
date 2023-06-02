from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Product, Category, Newsletter, Coupen, Reviews
from django.contrib import messages
from accounts.models import Cart, CartItems, MyOrders
from django.contrib.auth.decorators import login_required
import razorpay
from django.conf import settings
from django.utils import timezone

# Create your views here.

def shop(request):
    Categories = Category.objects.all()
    products = Product.objects.all()

    # Fetching with Category and Sorting

    if request.GET.get('category') and request.GET.get('sortBy'):
        category_fetch = request.GET.get('category')
        sort_factor = request.GET.get('sortBy')
        if category_fetch == "ALL":
            if sort_factor == "Default":
                products = Product.objects.all()
                return render(request, "shop/index.html", {'products':products,'category':Categories})
            if sort_factor == "Popularity":
                products = Product.objects.all().order_by('-buy_count')
                return render(request, "shop/index.html", {'products':products,'category':Categories, 'checked_sort':sort_factor})
            if sort_factor == "Price - Low to High":
                products = Product.objects.all().order_by('price')
                return render(request, "shop/index.html", {'products':products,'category':Categories, 'checked_sort':sort_factor})
            if sort_factor == "Price - High to Low":
                products = Product.objects.all().order_by('-price')
                return render(request, "shop/index.html", {'products':products,'category':Categories, 'checked_sort':sort_factor})
        category_obj = Category.objects.get(cat_name=category_fetch)
        products = Product.objects.filter(category=category_obj)
        if sort_factor == "Default":
            return render(request, "shop/index.html", {'products':products,'category':Categories,'checked_category':category_fetch})
        if sort_factor == "Popularity":
            products = products.order_by('-buy_count')
            return render(request, "shop/index.html", {'products':products,'category':Categories, 'checked_category':category_fetch, 'checked_sort':sort_factor})
        if sort_factor == "Price - Low to High":
            products = products.order_by('price')
            return render(request, "shop/index.html", {'products':products,'category':Categories,'checked_category':category_fetch, 'checked_sort':sort_factor})
        if sort_factor == "Price - High to Low":
            products = products.order_by('-price')
            return render(request, "shop/index.html", {'products':products,'category':Categories,'checked_category':category_fetch, 'checked_sort':sort_factor})
        

    # Fetching Products by Category

    if request.GET.get('category'):
        category_fetch = request.GET.get('category')
        if category_fetch == "ALL":
            return render(request, "shop/index.html", {'products':products,'category':Categories})
        category_obj = Category.objects.get(cat_name=category_fetch)
        products = Product.objects.filter(category=category_obj)
        return render(request, "shop/index.html", {'products':products,'category':Categories, 'checked_category':category_fetch})
    
    # Sorting Products 

    if request.GET.get('sortBy'):
        sort_factor = request.GET.get('sortBy')

        # Sorting by Popularity

        if sort_factor == "Popularity":
            products = Product.objects.all().order_by('-buy_count')
            return render(request, "shop/index.html", {'products':products,'category':Categories, 'checked_sort':sort_factor})

        # Sorting by Price - Low to High

        if sort_factor == "Price - Low to High":
            products = Product.objects.all().order_by('price')
            return render(request, "shop/index.html", {'products':products,'category':Categories, 'checked_sort':sort_factor})

        # Sorting by Price - High to Low

        if sort_factor == "Price - High to Low":
            products = Product.objects.all().order_by('-price')
            return render(request, "shop/index.html", {'products':products,'category':Categories, 'checked_sort':sort_factor})

    # Searching Algorithms for searching

    if request.GET.get('query'):
        query = request.GET.get('query')
        all_prods_name = Product.objects.filter(prod_name__icontains = query)
        all_prods_descp = Product.objects.filter(description__prod_descp__icontains=query)
        searchResult = all_prods_name | all_prods_descp
        updatedSearchResults = searchResult.distinct()
        return render(request, "shop/index.html", {'products':updatedSearchResults, 'query':query})

    return render(request, "shop/index.html", {'products':products,'category':Categories})

def prodDescp(request,slug):
    try:
        product = Product.objects.get(slug=slug)
        if request.method == "POST":
            if request.user.is_authenticated:
                review = request.POST.get("review_message")
                current_time = timezone.now()
                product_review = Reviews(product=product, user=request.user, review=review, publish_date=current_time)
                product_review.save()
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            else:
                messages.warning(request, "Login First")
                return redirect("/accounts/login")
        reviews = Reviews.objects.filter(product=product)
        return render(request, "shop/product_descp.html",{'prodDescp':product, 'reviews':reviews, 'product':product})

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

def cart(request, uid):
    if(request.user.is_authenticated):        
        product = Product.objects.get(uid=uid)
        user = request.user
        cart, _ = Cart.objects.get_or_create(user=user, is_paid=False)
        all_cart_items = CartItems.objects.filter(cart=cart)
        cart_items = CartItems.objects.create(cart=cart, product=product)
        if all_cart_items:
            for cart_item in all_cart_items:
                if cart_item.product.uid == product.uid:
                    if cart_item.quantity >= cart_item.product.product_available_count:
                        cart_items.delete()
                        messages.warning(request, f"Only {cart_item.product.product_available_count} items are available")
                        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
                    if cart_item.quantity == 0:
                        cart_item.quantity += 1
                        cart_item.save()
                        cart.cart_total_amount = cart.get_cart_total()
                        cart.save()
                    else:
                        cart_item.quantity += 1
                        cart_item.save()
                        cart_items.delete()
                        cart.cart_total_amount = cart.get_cart_total()
                        cart.save()
                    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        # cart_items.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    messages.warning(request, "LogIn for adding your items to cart")
    return redirect("/accounts/login")

def cartView(request):
    if(request.user.is_authenticated):
        carts = Cart.objects.filter(is_paid = False, user = request.user)
        cart_items = []
        delete = False
        for cart in carts:
            for cart_item in cart.cart_items.all():
                if cart_item.product.product_available_count > 0:
                    cart_items.append(cart_item)
                else:
                    cart_item.delete()
                    delete = True

        # Delivery Page

        if request.method == "POST" and request.POST.get("cost_of_cart"):
            cart = carts.first()
            cost_of_cart = cart.get_cart_total()
            cost_of_cart_without_coupon = cart.get_cart_total_without_coupen(cart.razorpay_order_id)
            if cart.city:
                # Razorpay
                client = razorpay.Client(auth=(settings.KEY, settings.SECRET))
                data = { "amount": carts.first().get_cart_total()*100, "currency": "INR", "payment_capture": 1 }
                payment = client.order.create(data=data)
                carts.first().set_razorpay_order_id(payment['id'])
                if delete:
                    messages.warning(request, "Product(s) That are not available are automatically removed Your Purchase List")
                    return render(request, 'shop/delivery_details.html', {'cart_items': cart_items, 'cost_of_cart':cost_of_cart, 'cart':cart, 'payment':payment, 'cost_of_cart_without_coupon':cost_of_cart_without_coupon})
                return render(request, 'shop/delivery_details.html', {'cart_items': cart_items, 'cost_of_cart':cost_of_cart, 'cart':cart, 'payment':payment, 'cost_of_cart_without_coupon':cost_of_cart_without_coupon})
            if delete:
                messages.warning(request, "Product(s) That are not available are automatically removed Your Purchase List")
                return render(request, 'shop/delivery_details.html', {'cart_items': cart_items, 'cost_of_cart':cost_of_cart, 'cart':cart, 'cost_of_cart_without_coupon':cost_of_cart_without_coupon})
            return render(request, 'shop/delivery_details.html', {'cart_items': cart_items, 'cost_of_cart':cost_of_cart, 'cart':cart, 'cost_of_cart_without_coupon':cost_of_cart_without_coupon})

        # Updating Delivery Details

        if request.method == "POST" and request.POST.get("first_name"):
            cost_of_cart = request.POST.get("cost_of_cart_update")
            first_name = request.POST.get("first_name")
            last_name = request.POST.get("last_name")
            email = request.POST.get("email")
            phone = request.POST.get("phone")
            address = request.POST.get("address")
            city = request.POST.get("city")
            state = request.POST.get("state")
            pincode = request.POST.get("pincode")
            country = request.POST.get("country")
            cart = carts.first()
            cart.first_name = first_name
            cart.last_name = last_name
            cart.email = email
            cart.phone = phone            
            cart.address = address
            cart.city = city
            cart.state = state
            cart.pincode = pincode
            cart.country = country
            if (request.POST.get("phone2")):
                phone2 = request.POST.get("phone2")
                cart.phone2 = phone2
            if (request.POST.get("address2")):
                address2 = request.POST.get("address2")
                cart.address2 = address2
            cost_of_cart_without_coupon = cart.get_cart_total_without_coupen(cart.razorpay_order_id)
            cart.save()
            # Razorpay
            client = razorpay.Client(auth=(settings.KEY, settings.SECRET))
            data = { "amount": carts.first().get_cart_total()*100, "currency": "INR", "payment_capture": 1 }
            payment = client.order.create(data=data)
            carts.first().set_razorpay_order_id(payment['id'])
            return render(request, 'shop/delivery_details.html', {'cart_items': cart_items, 'cost_of_cart':cost_of_cart, 'cart':cart, 'payment':payment, 'cost_of_cart_without_coupon':cost_of_cart_without_coupon})      

        # Coupen
        if request.method == 'POST' and request.POST.get("coupen"):

            if carts:
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
            messages.warning(request, "Cart is Empty")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        cart = carts.first()
        return render(request, 'shop/add_to_cart.html', {'cart_items': cart_items, 'cart':cart})

    messages.warning(request, "LogIn First")
    return redirect('/accounts/login')

@login_required(login_url="/accounts/login")
def success(request):
    if request.method == "POST":
        order_id = request.POST.get('order_ID')
        amount = request.POST.get('amount')
        payment_id = request.POST.get('payment_id')
        signature = request.POST.get('signature')
        cart = Cart.objects.filter(razorpay_order_id=order_id).first()
        if cart:
            if cart.get_cart_total()*100 != int(amount):
                return HttpResponse("Amount Mismatch")
            if cart.razorpay_order_id != order_id:
                return HttpResponse("Order ID Mismatch")
            cart.is_paid = True  
            cart.paid_cart_quantity = request.user.profile.get_cart_count()
            for product in cart.cart_items.all():
                product.product.set_product_available_count(product.quantity)
                product.product.set_buy_count(product.quantity)
            cart.publish_date = timezone.now()
            cart.set_payment_done_amount(amount[0:-2])
            cart.razorpay_payment_id = payment_id
            cart.razorpay_payment_signature = signature
            cart.save()
            save_my_order = MyOrders(user=request.user, cart=cart)
            save_my_order.save()
            return render(request, 'shop/payment_successful.html', {'order_id':order_id, 'amount':amount[0:-2]})
    return HttpResponse("404 Error")

def remove_cart(request, cart_item_uid):
    try:
        cart_item = CartItems.objects.get(uid=cart_item_uid)
        cart_item.delete()
    except Exception as e:
        print(e)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def delete_review(request, review_id):
    try:
        review = Reviews.objects.get(uid=review_id)
        review.delete()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    except Exception as e:
        print(e)
        return HttpResponse("404 Not Found")
    
def update_cart_quantity(request, cart_item_uid):
    try:
        cart_item = CartItems.objects.get(uid=cart_item_uid)
        if request.method == "POST":
            quantity = request.POST.get("quantity")
            if cart_item.product.product_available_count < int(quantity):
                messages.warning(request, f"Only {cart_item.product.product_available_count} items are available")
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            if int(quantity) <= 0:
                messages.warning(request, f"Quantity should be greater than 0")
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            cart_item.quantity = quantity
            cart_item.save()
            cart = cart_item.cart
            cart.cart_total_amount = cart.get_cart_total()
            cart.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    except Exception as e:
        return HttpResponse("404 Not Found")
    

def remove_coupon(request, coupon_uid):
    try:
        cart = Cart.objects.filter(user=request.user, is_paid=False).first()
        cart.coupen = None
        cart.save()
        messages.success(request, "Coupen Removed Successfully!")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    except Exception as e:
        return HttpResponse("404 Not Found") 