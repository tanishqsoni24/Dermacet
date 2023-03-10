from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def shop(request):
    return render(request, "shop/index.html")

def prodDescp(request):
    return render(request, "shop/product_descp.html")