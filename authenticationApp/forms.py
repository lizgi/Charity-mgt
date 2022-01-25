from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.contrib.auth import authenticate, get_user_model
from django.utils.text import capfirst

from authenticationApp.models import *


class DonorSignUp(UserCreationForm):
    first_name= forms.CharField(label='First Name' ,error_messages={'required': 'Please enter your first name'})
    last_name= forms.CharField(label='Last Name',error_messages={'required': 'Please enter your last name'})
    email= forms.EmailField(label='Email Address' ,help_text='Format: 123@gmail.com, 456@yahoo.com',error_messages={'required': 'Please enter your email address'})

    class Meta(UserCreationForm.Meta):
        model = User
        fields=['first_name','last_name','username','email','password1','password2']
        
        
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_donor=True
        user.save()
        donor = Donors.objects.create(user=user)
        donor.first_name = self.cleaned_data.get('first_name')
        donor.last_name = self.cleaned_data.get('last_name')
        donor.email = self.cleaned_data.get('email')
        return user
    
    
class NgoSignUp(UserCreationForm):
    organization_name= forms.CharField(label='Name of organization' ,error_messages={'required': 'Please enter your first name'})
    phone_number= forms.IntegerField(label='Phone number',error_messages={'required': 'Please enter your last name'})
    email= forms.EmailField(label='Email Address' ,help_text='Format: 123@gmail.com, 456@yahoo.com',error_messages={'required': 'Please enter your email address'})

    class Meta(UserCreationForm.Meta):
        model = User
        fields=['organization_name','username','phone_number','email','password1','password2']

        
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_ngo=True
        user.save()
        ngo =Ngo.objects.create(user=user)
        ngo.organization_name = self.cleaned_data.get('organization_name')
        ngo.username = self.cleaned_data.get('phone_number')
        ngo.email = self.cleaned_data.get('email')
        return user
    
    
    
    #login
class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class":"form-control"
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class":"form-control"
            }
        )
    )