from django.shortcuts import redirect, render,HttpResponse
from .models import *
from django.contrib.auth import authenticate, login, logout
from . import *
from datetime import date
from django.contrib.auth.decorators import login_required

# Create your views here.

def Index(request):
    return render(request, 'index.html')