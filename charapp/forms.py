from django import forms
from .models import NGO
from django.contrib.auth.models import User
from .models import Profile

class NGO_form(forms.ModelForm):
    class Meta:
        model = NGO
        fields = ('ngo_name','head_of_ngo','contactNo','email')



class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
