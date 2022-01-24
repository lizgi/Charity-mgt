
from django.urls import path
from . import views


urlpatterns=[
   
    path('signup/', views.signup,name='signUp'),
    path('signup/donors/', views.donor_signup,name='customer_signup'),
    path('signup/NGO/', views.ngo_signup,name='author_signup'),
    
]