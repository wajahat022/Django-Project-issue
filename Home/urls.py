from django.contrib import admin
from django.urls import path
from Home import views

urlpatterns = [
   path("", views.index, name= 'Home'),
   path("About", views.About, name= 'About'),
   path("Services", views.Services, name= 'Services'),
   path("Contact", views.Contact, name= 'Contact'),
]
