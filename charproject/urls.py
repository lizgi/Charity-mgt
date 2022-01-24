"""charproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
<<<<<<< HEAD
from xml.dom.minidom import Document
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from charapp import views as user_views
=======

from django.contrib import admin
from django.urls import path,include
from django.contrib import admin
>>>>>>> 1de695d9b89a0da794092334e7b4b560c26b3e90

urlpatterns = [
    path('profile/', user_views.profile, name='profile'),
    path('admin/', admin.site.urls),
    path('', include ('charapp.urls')),
    path('', include ('authenticationApp.urls')),
    path('', include('django.contrib.auth.urls')),

]

<<<<<<< HEAD
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
=======

>>>>>>> 1de695d9b89a0da794092334e7b4b560c26b3e90
