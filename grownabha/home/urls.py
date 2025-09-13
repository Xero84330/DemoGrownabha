from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.login_view , name='login'),
    path('signup/', views.signup_view , name='signup'),
    path('dashboard/',views.dashboard, name='dashboard'),
    path('lectures/', views.lectures, name='lectures')
]