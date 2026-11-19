from django.contrib import admin
from django.urls import path,include
from myapp import views

urlpatterns = [
    path('', views.index),
    path('dbdata/', views.dbdata,name="dbdata"),
]   
