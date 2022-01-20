from django.shortcuts import render, redirect

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

