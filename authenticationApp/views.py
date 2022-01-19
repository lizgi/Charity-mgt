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


