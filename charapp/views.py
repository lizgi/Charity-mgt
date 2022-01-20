from django.shortcuts import render, redirect
from .forms import NGO_form , donation_form


# Create your views here.
def donation(request):
    if request.method == 'POST':
        form = donation_form(request.POST, request.FILES)
        if form.is_valid():
            # form.save()
            return redirect('/')
    else:
        form = donation_form()

    return render(request, "CharitySystem/request_form.html",{'form':form})
