from django.urls import path
from . import views

urlpatterns = [
    path('', views.redirect_to_home, name='redirect_to_home'),
    path('home/', views.home, name='home'),
]