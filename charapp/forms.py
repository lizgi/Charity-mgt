from .models import  donation_request
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile




from .models import  donation_request,NGO
from django import forms

class donation_form(forms.ModelForm):
    class Meta:
        model = donation_request
        fields = ('donation_description','donation_amount', 'donation_category')

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
        fields = ('ngo_name','head_of_ngo','contactNo','email')

