from django.shortcuts import render
from django.http import HttpResponse


def login(request):
    return render(request, "accounts/login.html") 

def signup(request):
    return render(request, "accounts/signup.html") 