from django.test import TestCase
from .models import User

# Create your tests here.
class UserTestClass(TestCase):
    def setUp(self):
        user = User.objects.create(username="test_user")
        
