from django.urls import path
from . import views


urlpatterns = [ 
    path('ngo/', views.ngo)
from .views import Index
from . import views

urlpatterns = [
    path('', Index, name='index'),
]