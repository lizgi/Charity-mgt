from django.db import models
from django_currentuser.middleware import get_current_user, get_current_authenticated_user

# Create your models here.
class donation_request(models.Model):

    donation_description = models.TextField(blank=True,default=None)
    donation_amount = models.CharField(default=None,blank=True,max_length=15)
    donation_request_user = models.CharField(blank=True,default=get_current_authenticated_user,max_length=30)

    def __str__(self):
        return self.donation_amount
