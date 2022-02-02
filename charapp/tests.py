from django.test import TestCase
from .models import *
from django.contrib.auth.models import User

# Create your tests here.

class CategoryTestClass(TestCase):
    def setUp(self):
        self.category = Category(name='Test Category')

    def test_instance(self):
        self.assertTrue(isinstance(self.category, Category))

    def test_save_method(self):
        self.category.save()
        categories = Category.objects.all()
        self.assertTrue(len(categories) > 0)  

    def test_delete_method(self):
        self.category.save()
        self.category.delete_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) == 0)  

# class ProfileTestClass(TestCase):
#     # Set up method
#     def setUp(self):
#         self.user = User(username="liz", password="1122liz3.")
#         self.user.save()

#     def test_instance(self):
#         self.assertTrue(isinstance(self.profile,Profile))   
# 

class donation_requestTestClass(TestCase):
    def setUp(self):
        self.donation_request = donation_request(ngo_name='Test donation_request ')

    def test_instance(self):
        self.assertTrue(isinstance(self.donation_request, donation_request))

    def test_save_method(self):
        self.donation_request.save()
        donation_requests= donation_request.objects.all()
        self.assertTrue(len(donation_requests) > 0)  

    def test_delete_method(self):
        self.donation_request.save()
        self.donation_request.delete_donation_request()
        donation_requests = donation_request.objects.all()
        self.assertTrue(len(donation_requests) == 0) 


class CharityUserTestClass(TestCase):
    def setUp(self):
        self.category = CharityUser(name='Test Category')

    def test_instance(self):
        self.assertTrue(isinstance(self.category, CharityUser))

class DonorTestClass(TestCase):
    def setUp(self):
        self.Donor = Donor(username='Test Category')

    def test_instance(self):
        self.assertTrue(isinstance(self.Donor, Donor))



