from distutils.command.upload import upload
from email.mime import image
from email.policy import default
from django.conf import settings

from pyexpat import model
from tkinter import CASCADE
from django.db import models
from django_currentuser.middleware import get_current_user, get_current_authenticated_user
from django.contrib.auth.models import User
from PIL import Image


# Create your models here.

class donation_request(models.Model):

    donation_description = models.TextField(blank=True,default=0)
    donation_amount = models.CharField(default=None,blank=True,max_length=15)
    donation_request_user = models.CharField(blank=True,default=0,max_length=30)

    def __str__(self):
        return self.donation_amount



class Profile(models.Model):
    user = models.OneToOneField(to=settings.AUTH_USER_MODEL, on_delete=CASCADE)
    image = models.ImageField(default = 'default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'


    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
      
class NGO(models.Model):
    ngo_name = models.CharField(max_length=30,blank=True)
    domain = models.CharField(max_length=20,blank=True)
    head_of_ngo = models.CharField(max_length=30,blank=True)
    contactNo = models.CharField(max_length=10,blank=True)
    email = models.EmailField(blank=True)
    
    def __str__(self):
        return self.ngo_name

class donation_request_view(models.Model):
    ngo_name = models.CharField(default=None,max_length=50,blank=False,primary_key=True)
    domain = models.CharField(default=None,max_length=50,blank=False)
    head_of_ngo = models.CharField(default=None,max_length=50,blank=False)
    contactNo = models.CharField(default=None,max_length=10,blank=False)
    email = models.EmailField(blank=False,default=None)
    donation_description = models.TextField(default=None,blank=False)
    donation_amount = models.CharField(default=None,max_length=10,blank=False)

    def __str__(self):
        return self.ngo_name

    class Meta:
        managed = False
        db_table = 'post_request'    