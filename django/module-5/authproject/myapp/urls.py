from django.contrib import admin
from django.urls import path, include
from myapp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('usersignup/', views.usersignup, name='usersignup'),
    path('home/', views.home, name='home'),
]