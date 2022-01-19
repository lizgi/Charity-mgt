from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate

# Create your views here.


def signup(request):
    '''View function to present users with account choices'''
    title = 'Sign Up'
    return render(request,'registration/signup.html',{'title': title})