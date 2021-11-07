from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('support/',views.support,name='support'),
    path('about/',views.about,name='about'),
]