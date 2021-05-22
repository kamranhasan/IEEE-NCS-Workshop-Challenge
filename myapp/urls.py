from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from . import views

urlpatterns = [
    url(r'^$', views.home, name='index'),
    url(r'contacted$', views.contacted, name='contacted'),
    url(r'booked$', views.booked, name='booked'),
    url(r'checked$', views.checked, name='checked'),
    
]
