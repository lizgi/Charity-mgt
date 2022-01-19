from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from .forms import *

# Create your views here.


def signup(request):
    '''View function to present users with account choices'''
    title = 'Sign Up'
    return render(request,'registration/signup.html',{'title': title})


def donor_signup(request):
    '''View function to sign up as a donor'''
    if request.method == 'POST':
        form = DonorSignUp(request.POST)
        if form.is_valid():
            user = form.save()
            unhashed_password= form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=unhashed_password)
            login(request, user)
            subject = 'Welcome to the CHARITY APP!'
            message = f'Hi {user.first_name},\nThe Charity app would like to officially welcome you to our growing community.\nRemember to enjoy the app!\n\nKind Regards,\nThe Charity App Management.'
            email_from = settings.EMAIL_HOST_USER
            recepient_list = [user.email,]
            # send_mail(subject,message,email_from,recepient_list)
            messages.success(request, 'Account created successfully! Check your email for a welcome mail.')

            return redirect('/')
    else:
        form= DonorSignUp()

    title = 'Donors Sign Up'
    return render(request,'registration/signup_form.html',{'title': title,'form':form})

#NGO signup function
def ngo_signup(request):
    '''View function to sign up as an Ngo'''
    if request.method == 'POST':
        form = NgoSignUp(request.POST)
        if form.is_valid():
            user = form.save()
            unhashed_password= form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=unhashed_password)
            login(request, user)
            subject = 'Welcome to the BOOKSTORE!'
            message = f'Hi {user.first_name},\nThe Charity would like to officially welcome you to our growing  community.\nRemember to enjoy the app!\n\nKind Regards,\nThe Charity App Management.'
            email_from = settings.EMAIL_HOST_USER
            recepient_list = [user.email,]
            # send_mail(subject,message,email_from,recepient_list)
            messages.success(request, 'Account created successfully! Check your email for a welcome mail.')

            return redirect('/')
    else:
        form= NgoSignUp()

    title = 'ngo Sign Up'
    return render(request,'registration/signup_form.html',{'title': title,'form':form})
