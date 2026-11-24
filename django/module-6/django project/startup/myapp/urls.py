from django.contrib import admin
from django.urls import path, include
from myapp import views

urlpatterns = [
    path('', views.index),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('features/', views.features, name='features'),
    path('qoute/', views.qoute, name='qoute'),
    path('service/', views.service, name='service'),
    path('team/', views.team, name='team'),
    path('testimonial/', views.testimonial, name='testimonial'),

]