from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser

#create custoclass User(AbstractUser):
class User(AbstractUser):
    is_donor = models.BooleanField(default=False)
    is_ngo = models.BooleanField(default=False)
    
class Donors(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    
class Ngo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)