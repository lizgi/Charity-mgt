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
        user.is_ngo=True
        user.save()
        author = Ngo.objects.create(user=user)
        author.first_name = self.cleaned_data.get('first_name')
        author.last_name = self.cleaned_data.get('last_name')
        author.email = self.cleaned_data.get('email')
        return user