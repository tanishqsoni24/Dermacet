from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from .models import Profile

def login(request):
    if(request.method=="POST"):
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user_obj = User.objects.filter(username = email)
        if not user_obj.exists():
            messages.success(request, "Account doesn't exists")
            return HttpResponseRedirect(request.path_info)
        
        if not user_obj[0].profile.is_email_verified:
            messages.success(request, "Account Not Verified")
            return HttpResponseRedirect(request.path_info)

        user_obj = authenticate(username = email, password = password)
        if user_obj:
            login(request, user_obj)
            return redirect("/")

        messages.warning(request, "Invalid Credentials")
        return HttpResponseRedirect(request.path_info)
    return render(request, "accounts/login.html") 

def signup(request):
    if(request.method=="POST"):
        full_Name = request.POST.get('full_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user_obj = User.objects.filter(username = email)
        if user_obj.exists():
            messages.success(request, "Email already exists")
            return HttpResponseRedirect(request.path_info)
        user_obj = User.objects.create_user(full_Name , email, password)
        user_obj.save()

        messages.success(request, "An Email has been sent to your registered mail id")
        return HttpResponseRedirect(request.path_info)
    return render(request, "accounts/signup.html")