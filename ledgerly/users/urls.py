from django.urls import path
from . import views

urlpatterns = [
    path('', views.signIn, name='signin'),
    path('sign-up', views.signUp, name='signup'),
]