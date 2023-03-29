from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product, Category, Newsletter
from django.contrib import messages

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
        return HttpResponse("404 Not Found")

def manageNewsLetter(request):
    print("done till here bro")
    if request.method == "POST":    
        email = request.POST.get("email")
        newslettersave = Newsletter(email=email)
        newslettersave.save()
        messages.success(request, "Email Sent Successfully!")
        return redirect("/#contactus")
    else:
        return HttpResponse("500 FOUND")

def manageSearch(request):
    query = request.GET.get("query")
    all_prods_name = Product.objects.filter(prod_name__icontains = query)
    all_prods_descp = Product.objects.filter(prod_descp__icontains = query)
    searchResult = all_prods_name | all_prods_descp
    print(searchResult)
    return render(request, "shop/index.html", {'products':searchResult, 'query':query})
