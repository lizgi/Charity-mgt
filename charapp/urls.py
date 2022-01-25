

from . import views
from django.urls import path
from .views import Index, RequestList

urlpatterns = [
    path('', Index, name='index'),
    path('donation/', views.donation),
    path('blog/', views.blog, name='blog'),
    path('ngo/', views.ngo),
    path('gallery/', views.gallery, name='gallery'),
    path('contact/', views.Contact, name='contactUs'),
    path('requests/', RequestList.as_view()),

]

    


