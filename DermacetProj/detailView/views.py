from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Contact, Career
from accounts.models import Profile

# Create your views here.

def index(request):
    return render(request, "detailView/index.html")

def contctus(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        msg = request.POST.get("message")
        contact_data = Contact(name=name, email=email, message=msg)
        contact_data.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    return render(request, "detailView/contactus.html")

def career(request):
    if request.method == "POST" and request.FILES['CV']:
        name = request.POST['name']
        email = request.POST['email']
        cv = request.FILES['CV']
        career_data = Career(name=name, email=email, cv=cv)
        career_data.save()
        profile = Profile.objects.filter(user=request.user).first()
        profile.is_cv_uploaded = True
        profile.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    if list(Profile.objects.filter(user=request.user).values('is_cv_uploaded'))[0].get('is_cv_uploaded'):
        return render(request, "detailView/career.html", {'is_cv_uploaded':True})
    return render(request, "detailView/career.html")