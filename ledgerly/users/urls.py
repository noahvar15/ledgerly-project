from django.urls import path
from django.contrib.auth import views as auth_views 
from . import views

urlpatterns = [
    path('', views.logIn, name='login'),
    path('signup', views.signUp, name='signup'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('connect-coinbase/', views.connect_coinbase, name='connect_coinbase'),
    path('oauth/callback/', views.coinbase_callback, name='coinbase_callback'),
    path('disconnect-coinbase/', views.disconnect_coinbase, name='disconnect_coinbase'),
]