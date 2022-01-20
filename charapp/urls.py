
from . import views
from django.urls import path


urlpatterns = [ 
    path('', views.donation),
    path('blog/', views.blog),,
    path('ngo', views.ngo),
    path('gallery', views.gallery),
]

