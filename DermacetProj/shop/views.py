from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Category

# Create your views here.

def shop(request):
    Categories = Category.objects.all()
    products = Product.objects.all()
    return render(request, "shop/index.html", {'products':products,'category':Categories})

def prodDescp(request,slug):
    try:
        product = Product.objects.get(slug=slug)
        return render(request, "shop/product_descp.html",{'prodDescp':product})

    except Exception as e:
        print(e)
