from django.test import TestCase
import unittest
from models import Donors

# Create your tests here.
class TestDonors(unittest.TestCase):
    def setUp(self):
        self.new_user = Donors('Timothy', '9000T')
        
        
    def test_init(self):
        self.assertEqual(self.new_user.username, 'Timothy')
        self.assertEqual(self.new_user.password, '9000T')
    
    def test_save_donors(self):
        self.new_user.save_user()
        self.assertEqual(len(Donors.user_list), 1)