from django.db import models

# Create your models here.
class NGO(models.Model):
    ngo_name = models.CharField(max_length=30,blank=True)
    domain = models.CharField(max_length=20,blank=True)
    head_of_ngo = models.CharField(max_length=30,blank=True)
    contactNo = models.CharField(max_length=10,blank=True)
    email = models.EmailField(blank=True)