from django.shortcuts import render, redirect
from django.contrib import messages
# from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm, ProfileUpdateForm
from charapp.forms import NGO_form

# Create your views here.

def ngo(request):
    if request.method == 'POST':
        form = NGO_form(request.POST, request.FILES)
        if form.is_valid():
            # form.save()
            return redirect('http://127.0.0.1:8000/')
    else:
        form = NGO_form()

    return render(request,"verify.html",{'form':form})

# @login_required
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
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'profilee.html', context)