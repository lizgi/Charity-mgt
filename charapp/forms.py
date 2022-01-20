from .models import  donation_request
from django import forms




class donation_form(forms.ModelForm):
    class Meta:
        model = donation_request
        fields = ('donation_description','donation_amount')
