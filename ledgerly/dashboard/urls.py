from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.index, name='dashboard-home'),
    path('analytics/', views.analytics, name='dashboard-analytics'),
]