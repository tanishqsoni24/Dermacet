from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import login as auth_login
from django.http import HttpResponse
from .models import Profile

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
        
        user_obj = User.objects.filter(username = email)
        if user_obj.exists():
            messages.error(request, "Email already exists")
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