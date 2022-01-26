from django.shortcuts import render, redirect
from .forms import  donation_form
from .forms import  UserUpdateForm, ProfileUpdateForm
# from django.contrib.auth.decorators import login_required
from django.contrib import messages


from django.shortcuts import render, redirect,HttpResponse

from .forms import  donation_form,NGO_form
from .models import *
from . import *
from datetime import date
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView


# Create your views here.
def Index(request):
    return render(request,'index.html')
    
def donation(request):
    if request.method == 'POST':
        form = donation_form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            ngorequest=form.save()
            ngorequest.save()
            return redirect('/')
    else:
        form = donation_form()

    return render(request, "request_form.html",{'form':form})

def ngorequests(request):
    ngorequest = donation_request.objects.filter(admin_approved=True)

    return render(request, 'request_list.html', {'requests': ngorequest})

def blog(request):
    return render(request, 'blog.html')

def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm()
        p_form = ProfileUpdateForm()

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'profile.html', context)
def ngo(request):
    if request.method == 'POST':
        form = NGO_form(request.POST, request.FILES)
        if form.is_valid():
            # form.save()
            return redirect('/')
    else:
        form = NGO_form()

    return render(request,"verify.html",{'form':form})

def gallery(request):
    return render(request, 'gallery.html')

#Contact us function
def Contact(request):
    return render(request,'contact_us.html')

def not_verified(request):
    return render(request, "not_verified.html")

def verify_from_admin(request):
    data = NGO.objects.all()
    return render(request, "verify_from_admin.html", {'ngo':data})
def about(request):
    return render(request,'about.html')

def payment(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        charityusername = request.POST['charityusername']
        amount = request.POST['amount']

        # Saving Payment Details
        donation = NGO()
        donation.username = username
        donation.charityusername = charityusername
        donation.amount = amount
        donation.save()

        # Updating Variables
       
        #Successful Message
        messages.success(request, "Payment Successful") 
    return render(request,'payment.html')

