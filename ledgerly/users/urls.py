from django.urls import path
from . import views

urlpatterns = [
    path('', views.signIn, name='signin'),
    path('signup', views.signUp, name='signup'),
]