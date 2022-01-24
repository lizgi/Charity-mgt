from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

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
        user.is_customer=True
        user.save()
        donor = Donors.objects.create(user=user)
        donor.first_name = self.cleaned_data.get('first_name')
        donor.last_name = self.cleaned_data.get('last_name')
        donor.email = self.cleaned_data.get('email')
        return user
    
    
class NgoSignUp(UserCreationForm):
    first_name= forms.CharField(label='First Name' ,error_messages={'required': 'Please enter your first name'})
    last_name= forms.CharField(label='Last Name',error_messages={'required': 'Please enter your last name'})
    email= forms.EmailField(label='Email Address' ,help_text='Format: 123@gmail.com, 456@yahoo.com',error_messages={'required': 'Please enter your email address'})

    class Meta(UserCreationForm.Meta):
        model = User
        fields=['first_name','last_name','username','email','password1','password2']

        
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_author=True
        user.save()
        ngo =Ngo.objects.create(user=user)
        ngo.first_name = self.cleaned_data.get('first_name')
        ngo.last_name = self.cleaned_data.get('last_name')
        ngo.email = self.cleaned_data.get('email')
        return user