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

stripe.api_key = 'pk_test_51KMSP6KoSUQSUmrFIOOBDtlAciRFv0HLp9FiEHuOgICwA25UYnA3XFRohDDtq98PlLRbLSYjZSaUSoghHAtyqEps00LC97CniE'
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
@login_required(login_url='/accounts/login/')
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

def employerDash(request):
    current_user = request.user
    profile = Employer.objects.get(user_id=current_user.id)
    job_seekers = User.objects.filter(is_jobseeker=True).all()
    # potential = JobSeeker.objects.all()
    employer = User.objects.all()
    if request.method == 'POST':
        mpesa_form = PaymentForm(
            request.POST, request.FILES, instance=request.user)
        if mpesa_form.is_valid():
            mpesa_form.save()
            messages.success(
                request, 'Your Payment has been made successfully')
            return redirect('employerDash')
    else:
        mpesa_form = PaymentForm(instance=request.user)

    context = {
        # "potential": potential,
        "job_seekers": job_seekers,
        "employer": employer,
        'profile': profile,
        'mpesa_form': mpesa_form
    }
    return render(request, 'employer.html', context)



def employerPayment(request):
    current_user = request.user
    if request.method == 'POST':
        mpesa_form = PaymentForm(
            request.POST, request.FILES, instance=request.user)
        if mpesa_form.is_valid():
            mpesa_form.save()
            messages.success(
                request, 'Your Payment has been made successfully')
            return redirect('employerDash')
    else:
        mpesa_form = PaymentForm(instance=request.user)
    context = {
        'mpesa_form': mpesa_form,

    }
    return render(request, 'paymentform.html', context)



cl = MpesaClient()
stk_push_callback_url = ''
c2b_callback_url = ''


def oauth_success(request):
    r = cl.access_token()
    return JsonResponse(r, safe=False)


def stk_push_success(request):
    phone_number = config('LNM_PHONE_NUMBER')
    amount = 1
    account_reference = 'ABC001'
    transaction_desc = 'STK Push Description'
    callback_url = stk_push_callback_url
    r = cl.stk_push(phone_number, amount, account_reference,
                    transaction_desc, callback_url)
    return JsonResponse(r.response_description, safe=False)


def customer_payment_success(request):
    phone_number = config('C2B_PHONE_NUMBER')
    amount = 1
    transaction_desc = 'Customer Payment Description'
    occassion = 'Test customer payment occassion'
    callback_url = c2b_callback_url
    r = cl.business_payment(phone_number, amount,
                            transaction_desc, callback_url, occassion)
    return JsonResponse(r.response_description, safe=False)


def promotion_payment_success(request):
    phone_number = config('C2B_PHONE_NUMBER')
    amount = 1
    transaction_desc = 'Promotion Payment Description'
    occassion = 'Test promotion payment occassion'
    callback_url = b2c_callback_url
    r = cl.promotion_payment(phone_number, amount,
                             transaction_desc, callback_url, occassion)
    return JsonResponse(r.response_description, safe=False)
