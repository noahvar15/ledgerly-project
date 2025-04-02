from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    return render(request, 'dashboard/index.html', {})

@login_required
def analytics(request):
    return render(request, 'dashboard/analytics.html', {})

@login_required
def assets(request):
    return render(request, 'dashboard/assets.html', {})

@login_required
def transactions(request):
    return render(request, 'dashboard/transactions.html', {})

@login_required
def settings(request):
    return render(request, 'dashboard/dashboard-settings.html', {})