from .models import  donation_request
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile




from .models import  donation_request,NGO
from django import forms
from .models import NGO
from django.contrib.auth.models import User
from .models import Profile

class donation_form(forms.ModelForm):
    class Meta:
        model = donation_request
        fields = ('ngo_name', 'donation_description','donation_amount', 'Request_for_donation',)

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
class NGO_form(forms.ModelForm):
    class Meta:
        model = NGO
        fields = ('ngo_name','Amount',  'head_of_ngo','contactNo','email',)



class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
