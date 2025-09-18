from django.contrib import admin
from django.urls import path
from main import views

urlpatterns = [
    path('', views.home, name='home'),
    path('subject/', views.subject, name='subject'),
    path('chapter/', views.chapter, name='chapter'),
]