from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser

#create custoclass User(AbstractUser):
class User(AbstractUser):
    is_customer = models.BooleanField(default=False)
    is_author = models.BooleanField(default=False)