
from . import views
from django.urls import path
from .views import Index

urlpatterns = [
    path('', Index, name='index'),
    path('donation/', views.donation),
    path('blog/', views.blog, name='blog'),
    path('ngo/', views.ngo),
    path('gallery/', views.gallery, name='gallery'),
    path('contact/', views.Contact, name='contactUs'),
    path('about/', views.about, name='about'),
    path('payment/',views.payment,name = 'payment'),
    path('paymentt/', views.payment, name='paymentt'),
    path('requests/', views.ngorequests,name='ngorequests'),
    path('charge/', views.charge, name="charge"),
    path('donorprofile/', views.donor_profile, name='donorprofile'),

   

]


