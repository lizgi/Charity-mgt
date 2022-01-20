from django.shortcuts import render, redirect
from .forms import  donation_form


# Create your views here.
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
