from django import forms
from .models import NGO

class NGO_form(forms.ModelForm):
    class Meta:
        model = NGO
        fields = ('ngo_name','domain','head_of_ngo','contactNo','email')


