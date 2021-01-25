from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('vendors', views.vendor_list, name='vendor_list'),
    path('vendors/<int:pk>', views.vendor_detail, name='vendor_detail'),
    path('vendors/new', views.vendor_create, name='vendor_create'),
    path('vendors/<int:pk>/edit', views.vendor_edit, name='vendor_edit'),
    path('vendors/<int:pk>/delete', views.vendor_delete, name='vendor_delete')
]
