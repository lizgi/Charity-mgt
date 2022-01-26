from django.db import models
from PIL import Image
from django.conf import settings
from django.contrib.auth.models import User
from django_currentuser.middleware import get_current_user, get_current_authenticated_user

# Create your models here.

class donation_request(models.Model):

    donation_description = models.TextField(blank=True,default=0)
    donation_amount = models.CharField(default=None,blank=True,max_length=15)
    donation_request_user = models.CharField(blank=True,default=0,max_length=30)

    def __str__(self):
        return self.donation_amount
      
class NGO(models.Model):
    ngo_name = models.CharField(max_length=30,blank=True)
    head_of_ngo = models.CharField(max_length=30,blank=True)
    contactNo = models.CharField(max_length=10,blank=True)
    email = models.EmailField(blank=True)
    Amount = models.CharField(max_length=30,blank=True)
    Reason_for_donation= models.CharField(max_length=30,blank=True)
    verification_status = models.NullBooleanField(default=None,blank=True,null=True)
    ngo_current_user = models.CharField(default=0,blank=True,max_length=40)

    def verification_true(self):
        self.verification_status=True        
        self.save()

    def verification_false(self):
        self.verification_status = False
        self.save()

    def get_user(self,user):
        self.ngo_user = user
        self.save()

    def _str_(self):
        return self.ngo_name
class Profile(models.Model):
    user = models.OneToOneField(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
    
    def __str__(self):
        return self.ngo_name

