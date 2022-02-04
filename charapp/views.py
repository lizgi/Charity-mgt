from django.shortcuts import render, redirect
from authenticationApp.decorators import donor_required, ngo_required
from .forms import  donation_form
from django.contrib.auth.decorators import login_required

from .forms import  UserUpdateForm, ProfileUpdateForm
# from django.contrib.auth.decorators import login_required
from django.contrib import messages
import stripe
from django.shortcuts import render, redirect,HttpResponse
from .forms import  donation_form,NGO_form
from .models import *
from . import *
from datetime import date
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.http import HttpResponse, HttpResponseRedirect, Http404, JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from charapp.mpesa import utils
from . mpesa.core import MpesaClient
from decouple import config
from charapp.forms import PaymentForm
from datetime import datetime
import base64
import requests
import json


# Create your views here.
def Index(request):
    return render(request,'index.html')

@ngo_required(login_url='/login')
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

@donor_required(login_url='/login')
def ngorequests(request):
    ngorequest = donation_request.objects.filter(admin_approved=True)

    return render(request, 'request_list.html', {'requests': ngorequest})

def blog(request):
    return render(request, 'blog.html')

@ngo_required(login_url='/login')
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

    
    myrequest = donation_request.objects.filter(admin_approved=True)
    context = {
        'u_form': u_form,
        'p_form': p_form,
        'myrequests': myrequest
    }
    return render(request, 'profile.html', context)

@donor_required(login_url='/login')
def donor_profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('index')

    else:
        u_form = UserUpdateForm()
        p_form = ProfileUpdateForm()

    
    myrequest = donation_request.objects.filter(admin_approved=True)
    context = {
        'u_form': u_form,
        'p_form': p_form,
        'myrequests': myrequest
    }
    return render(request, 'donor_profile.html', context)


@ngo_required(login_url='/login')
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

@donor_required(login_url='/login')
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
    return render(request,'paymentt.html')

@donor_required(login_url='/login')
def payment(request):
    return render(request, 'paymentt.html')    

def charge(request):
    if request.method == 'POST':

        cus_name = request.POST["cus_name"]
        amount = request.POST["amount"]
        doantion_message = request.POST["message"]
        mail = request.POST["mail"]

        customer = stripe.Customer.create(
            email = mail,
            name = cus_name,
            # source = request.POST["stripeToken"]
        )

        charge = stripe.Charge.create (
            customer = customer,
            amount = int(amount)*100,
            currency = 'INR',
            description = doantion_message
        )

        return render(request, 'payment.html',{'amount':amount})


# m={
#     "paybill":"174379",
#     "passKey":"bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919",
#     "consumer_key":"mVCZ6HueP2soLBtsAG8GWyfF7R1D1ATm",
#     "consumer_secret":"xoEeo8whgW2fiYBN",
#     "BusinessShortCode": 174379,
#     "TransactionType": "CustomerPayBillOnline",
#     "PartyB": 174379,
#      "CallBackURL": "https://mydomain.com/path",
#     "AccountReference": "CompanyXLTD",
#     "TransactionDesc": "Payment of X"
# }
# def express_payload(amount,phone,passkey,time):
#     return {
#          "BusinessShortCode": 600978,
#          "Password":passkey,
#          "Timestamp":time,
#          "TransactionType": "CustomerPayBillOnline",
#           "Amount": amount,
#           "PartyA": phone,
#           "PartyB": 600978,
#           "PhoneNumber": phone,
#            "CallBackURL": "https://mydomain.com/path",
#          "AccountReference": "CompanyXLTD",
#         "TransactionDesc": "Payment of X"
#     }
# ## Function Below generates the mpesa password and time format.
# def mpesa_time_pass():
#     t=mpesa_time_stamp()
#     s=str(m["paybill"]+m["passKey"]+t).encode("ascii")
#     en=base64.b64encode(s)
#     print(en)
#     return {"time":str(t),"password":en.decode("ascii")}
# def mpesa_pass_key(timestamp):
#     en=str(str(m["BusinessShortCode"])+m["passKey"]+timestamp).encode("ascii")
#     return base64.b64encode(en).decode("ascii")
# def mpesa_time_stamp():
#    d=datetime.now()
#    x=d.strftime("%Y%m%d%H%M%S")
#    return x
# def mpesa_express(amount=1,phone=254725089717):
#     time=mpesa_time_stamp()
#     token=mpesa_token()
#     payload=express_payload(amount,phone,mpesa_pass_key(time),time)
#     print(payload)
#     url='https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest'
#     res=requests.post(url,headers={"Authorization":f"Bearer {token}"},data=payload)
#     print(res.text)
# #Function to generate mpesa token
# def mpesa_token():
#     s=str(m["consumer_key"]+":"+m["consumer_secret"]).encode("ascii")
#     mpesaKey=base64.b64encode(s)
#     #print(mpesaKey)
#     #print(mpesaKey.decode("ascii"))
#     newkey=mpesaKey.decode("ascii")
#     url="https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"
#     res=requests.get(url,headers={"Authorization":f"Basic {newkey}"})
#     k=json.loads(res.text)
#     return k["access_token"]
# # mpesa_time_pass()
# #print(mpesa_time_pass())
# #print(mpesa_token())
# mpesa_express()
# #print(mpesa_pass_key("34324234"))