from asyncio.base_futures import _PENDING
from django.db import models
from django_currentuser.middleware import get_current_user, get_current_authenticated_user

# Create your models here.

STATUS_CHOICES = [
    ('P', 'pending'),
    ('A', 'Approved'),
    ('w', 'Withdrawn'),
]

class donation_request(models.Model):

    donation_description = models.TextField(blank=True,default=None)
    donation_amount = models.CharField(default=None,blank=True,max_length=15)
    donation_request_user = models.CharField(blank=True,default=get_current_authenticated_user,max_length=30)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES,default=_PENDING)
    admin_approved = models.BooleanField(default=False)
    date_posted = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.donation_amount
      
class NGO(models.Model):
    ngo_name = models.CharField(max_length=30,blank=True)
    domain = models.CharField(max_length=20,blank=True)
    head_of_ngo = models.CharField(max_length=30,blank=True)
    contactNo = models.CharField(max_length=10,blank=True)
    email = models.EmailField(blank=True)
    
    def __str__(self):
        return self.ngo_name

