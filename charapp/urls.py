
from django.urls import path
from .views import Index
from . import views

urlpatterns = [
    path('', Index, name='index'),
]