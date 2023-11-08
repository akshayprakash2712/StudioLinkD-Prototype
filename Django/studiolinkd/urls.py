from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('signin/', views.signin, name='signin'),
    path('logout/', views.LogoutUser, name='logout'),
    path('home/', views.home, name='home'),
    path('artist/', views.artist, name='artist'),
    path('client/', views.client, name='client'),
    path('tv/', views.tv, name='tv'),
    path('radio/', views.radio, name='radio'),
    path('edit/', views.EditView, name='edit'),
    path('change_password/', views.change_password, name='change_password'),

    path('artist_list/', views.atrist_list, name='artist_list'),
    
    path('client_list/', views.client_list, name='client_list'),
    
    path('tv_list/', views.tv_list, name='tv_list'),
    
    path('radio_list/', views.radio_list, name='radio_list')
   
]
