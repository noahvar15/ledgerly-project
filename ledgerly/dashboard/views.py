from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'dashboard/index.html', {})

def analytics(request):
    return render(request, 'dashboard/analytics.html', {})

def assets(request):
    return render(request, 'dashboard/assets.html', {})

def transactions(request):
    return render(request, 'dashboard/transactions.html', {})

def settings(request):
    return render(request, 'dashboard/settings.html', {})