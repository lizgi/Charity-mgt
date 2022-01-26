
from . import views
from django.urls import path
from .views import Index
from django.conf.urls import url

urlpatterns = [
    path('', Index, name='index'),
    url(r'^fund_request/$', views.donation,name="fund request"),
    path('donation/', views.donation),
    path('blog/', views.blog, name='blog'),
    path('ngo/', views.ngo),
    path('gallery/', views.gallery, name='gallery'),
    path('contact/', views.Contact, name='contactUs'),


    path('about/', views.about, name='about'),



]

    


