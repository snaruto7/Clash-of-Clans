from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import views 

urlpatterns = [
    path('signin',views.signin,name='signin'),
    path('signup',views.signup,name='signup'),
    path('home',views.home,name='home'),
    path('signout',views.signout,name='signout'),
]