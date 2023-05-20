from django.contrib import admin
from .models import Contact, Career

# Register your models here.

admin.site.register((Contact, Career))