from django.contrib import admin
from django.urls import path, include
from myapp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('feature/', views.feature, name='feature'),
    path('quote/', views.quote, name='quote'),
    path('quote/new/<slug:service>/', views.create_quote, name='create_quote'),
    path('quote/<int:id>/bill/', views.quote_bill, name='quote_bill'),
    path('quote/<int:id>/edit/', views.edit_quote, name='edit_quote'),
    path('quote/<int:id>/delete/', views.delete_quote, name='delete_quote'),
    path('service/', views.service, name='service'),
    path('team/', views.team, name='team'),
    path('testimonial/', views.testimonial, name='testimonial'),
    path('search/', views.search, name='search'),
    path('subscribe/', views.subscribe, name='subscribe'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.user_logout, name='logout'),

]
