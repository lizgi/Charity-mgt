

from . import views
from django.urls import path
from .views import Index

urlpatterns = [
    path('', Index, name='index'),
    path('donation/', views.donation),
    path('blog/', views.blog),
    path('ngo', views.ngo),
    path('gallery', views.gallery),
    path('contact/', views.Contact, name='contactUs'),

]

    


