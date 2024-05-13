from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('',views.index,name='home'),
    path('index',views.index,name='home'),
    path('about',views.about,name = 'about'),
    path('services',views.services,name = 'services'),
    path('getstarted',views.getstarted,name = 'getstarted'),
    path('search',views.search,name = 'search')
    
]
   