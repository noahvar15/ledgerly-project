from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from services.coinbase_api import is_coinbase_connected
from django.contrib import messages

@login_required
def index(request):
    if request.user.is_authenticated and is_coinbase_connected(request.user):
        messages.success(request, "Coinbase account is connected.")
    else:
        messages.warning(request, "Coinbase is not connected.")
    
    return render(request, 'dashboard/index.html')

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