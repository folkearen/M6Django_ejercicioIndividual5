from django.contrib import admin
from django.urls import path
from . import views

app_name  = 'home'
urlpatterns = [
    path('', views.homePage, name="home"),
    path('contacto/', views.homeContacto, name="contacto")

]