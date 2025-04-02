from django.urls import path
from . import views

urlpatterns = [
    path('', views.logIn, name='login'),
    path('signup', views.signUp, name='signup'),
]