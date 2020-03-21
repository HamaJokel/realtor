from django.urls import path 

from . import views 

urlpatterns = [
    path('', views.index, name='index'), #The Homepage
    path('about', views.about, name='about'),   
]
