from django.urls import path
from stdata import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dbdata/', views.dbdata, name='dbdata'),
    path('update/<int:id>/', views.update, name='update'),
    path('delete/<int:id>/', views.delete, name='delete'),
]
