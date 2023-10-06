from django.contrib import admin
from django.urls import path
from .views import CustomerView, AboutView

urlpatterns = [
    path('create/', CustomerView.as_view(), name='create-customer'),
    path('info/', AboutView.as_view(), name='about-view' )
]