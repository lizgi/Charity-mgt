
from django.urls import path
from . import views


urlpatterns=[
   
    path('signup/', views.signup,name='signup'),
    path('signup/NGO/', views.donor_signup,name='customer_signup'),
    path('signup/donors/', views.ngo_signup,name='author_signup'),
    
]