from django.contrib import admin
from django.urls import path,include
from stdata import views

urlpatterns = [
    path('', views.index, name="index"),
    path('dbdata/', views.dbdata,name="dbdata"),
    path('dbdata/index', views.dbdata),
    path('update/<int:id>/', views.update, name="update"),
    path('delete/<int:id>/', views.delete, name="delete"),
]   
