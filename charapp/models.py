from asyncio.base_futures import _PENDING
from distutils.command.upload import upload
from email.mime import image
from email.policy import default
from django.conf import settings
from django.db import models
from PIL import Image
from django.conf import settings
from django.contrib.auth.models import User


# Create your models here.

STATUS_CHOICES = [
    ('P', 'pending'),
    ('A', 'Approved'),
    ('w', 'Withdrawn'),
]

  
#Category class
class Category(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def save_category(self): 
        self.save()

    def delete_category(self):
         self.delete()  


class Profile(models.Model):
    user = models.OneToOneField(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(default=0, upload_to='profile_pics')

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
    head_of_ngo = models.CharField(max_length=30,blank=True)
    contactNo = models.CharField(max_length=10,blank=True)
    email = models.EmailField(blank=True)
    Amount = models.CharField(max_length=30,blank=True)
    Reason_for_donation= models.CharField(max_length=30,blank=True)
    verification_status = models.NullBooleanField(default=0,blank=True,null=True)
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

   

class donation_request(models.Model):
    ngo_name = models.CharField(max_length=50,blank=False,primary_key=True)
    head_of_ngo = models.CharField(max_length=30,blank=True)
    contactNo = models.CharField(max_length=10,blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,null=True)
    email = models.EmailField(blank=False)
    donation_amount = models.CharField(default=0,blank=True,max_length=15)
    donation_request_user = models.CharField(blank=True,max_length=30)
    Reason_for_donation_request = models.CharField(blank=True,max_length=500)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES,default=_PENDING)
    admin_approved = models.BooleanField(default=False)




    def __str__(self):
        return self.donation_amount

    def delete_donation_request(self):
         self.delete()  
     

class CharityUser(models.Model):
    username = models.CharField(max_length = 100,primary_key = True) # Charity User_Name
    name = models.CharField(max_length = 100) # Charity Name
    description = models.TextField() # Short Description about Charity
    image = models.CharField(max_length=100)  # Path of Iamge
    donors = models.IntegerField(default=0) # No of donors Donated
    amount = models.IntegerField(default=0) # Total Amount of Donation Made
    
    def __str__(self):
        return self.name

class Donor(models.Model):
    username = models.CharField(max_length = 100) #UserName of Donor
    amount = models.IntegerField(default=0) # Amount Donated
    charityusername = models.CharField(max_length = 100) # Charity User Name to which it is donated

    def __str__(self):
        return self.username

class Subscribe(models.Model):
    first_name = models.CharField(max_length=144, null=True, blank=True)
    last_name = models.CharField(max_length=144, null=True, blank=True)
    contact = models.CharField(
        unique=True, max_length=20, null=True, blank=True)



class AccessToken(models.Model):
    token = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        get_latest_by = 'created_at'

    def __str__(self):
        return self.token
