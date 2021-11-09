from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),    
    path('',views.home,name='home'),
    path('contact/',views.contact,name='contact'),
    path('about/',views.about,name='about'),
    path('search/',views.search,name='search'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.login,name='login'),
]