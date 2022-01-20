
from .models import  donation_request,NGO
from django import forms

class donation_form(forms.ModelForm):
    class Meta:
        model = donation_request
        fields = ('donation_description','donation_amount'

class NGO_form(forms.ModelForm):
    class Meta:
        model = NGO
        fields = ('ngo_name','head_of_ngo','contactNo','email')

