from django.shortcuts import render
from .models import *

# Create your views here.

def home(request):
    return render(request,"hospital_admin/home.html")

def appointment(request):

    return render(request)
