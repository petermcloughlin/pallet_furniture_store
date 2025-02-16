from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.bespokerequest_view, name='bespokerequest'),     
]