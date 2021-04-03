from django.conf.urls import url
from irm_login import views

from django.urls import path 

urlpatterns = [
    url(r'^$', views.index),
    url('register/',views.register,name='register'),
    url('dashboard/',views.dashboard, name='dashboard'),
    url(r'^$', views.logout, name='logout'),
]
