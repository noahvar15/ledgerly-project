from django.urls import path
from . import views

urlpatterns = [
    path('', views.signIn, name='users-sign-in'),
    path('sign-up', views.signUp, name='users-sign-up'),
]