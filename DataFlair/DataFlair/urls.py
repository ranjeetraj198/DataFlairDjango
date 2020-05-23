"""DataFlair URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from .views import *
from django.views.generic.base import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/', include('student.urls')),
    path('demo/',include('demo.urls')),
    path('subscribe/', include('subscribe.urls')),
    path('registration/', include('registration.urls')),
    path('upload/', include('profile_maker.urls')),
    path('', include('home.urls')),
    path('ajax/', include('post.urls')),
    path('dataflair/', index),
    path('redirect/', data_flair),
    path('djangotutor/', RedirectView.as_view(url = 'https://www.gochatclub.com/')),
    path('inf1/', inf2),
    path('inf2/', inf1),
    path('setcookie/', setcookie),
    path('getcookie/', showcookie),
    path('deletecookie/', delete_co),
    path('testcookie/', cookie_session),
    path('deletecookie/', cookie_delete),
    path('create/', create_session),
    path('access/', access_session),
    path('delete/', delete_session),
]
