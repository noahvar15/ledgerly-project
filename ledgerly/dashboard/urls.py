from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='dashboard-home'),
    path('analytics/', views.analytics, name='dashboard-analytics'),
    path('assets/', views.assets, name='dashboard-assets'),
    path('transactions/', views.transactions, name='dashboard-transactios'),
    path('settings/', views.settings, name='dashboard-settings'),
]