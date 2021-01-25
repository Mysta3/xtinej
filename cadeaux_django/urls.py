"""xtine_vendorlist_django URL Configuration

The `urlpatterns` list routes URLs to views. 
"""
from django.conf.urls import include
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cadeaux.urls')),
    path('', include('accounts.urls'))
]
