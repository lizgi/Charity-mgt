from django.urls import path
from . import views


urlpatterns = [ 
    path('ngo', views.ngo),
    path('gallery', views.gallery)
]