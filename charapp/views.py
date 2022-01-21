
from django.shortcuts import render, redirect,HttpResponse
from .forms import  donation_form,NGO_form
from django.contrib.auth import authenticate, login, logout
from .models import *
from . import *
from datetime import date
from django.contrib.auth.decorators import login_required

# Create your views here.
def Index(request):
    return render(request,'index.html')
    
def donation(request):
    if request.method == 'POST':
        form = donation_form(request.POST, request.FILES)
        if form.is_valid():
            # form.save()
            return redirect('/')
    else:
        form = donation_form()

    return render(request, "request_form.html",{'form':form})

def blog(request):
    return render(request, 'blog.html')
def ngo(request):
    if request.method == 'POST':
        form = NGO_form(request.POST, request.FILES)
        if form.is_valid():
            # form.save()
            return redirect('http://127.0.0.1:8000/')
    else:
        form = NGO_form()

    return render(request,"verify.html",{'form':form})


def gallery(request):
    return render(request, 'gallery.html')

#Contact us function
def Contact(request):
    return render(request,'contact_us.html')
