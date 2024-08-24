from django.contrib import admin
from django.urls import path, include
from . import views





urlpatterns = [

    path ('', views.index),
    path ('new', views.new),
    path ("data", views.data),
    path ("test", views.test),
]