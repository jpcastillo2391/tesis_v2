from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from . import views

app_name = 'Login'

urlpatterns = [
    url(r'^$', views.home_page, name='Loginpage'),
]