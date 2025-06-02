import secrets, requests
from django.conf import settings
from django.shortcuts import render, redirect
from django.utils.timezone import now, timedelta
from django.contrib.auth.decorators import login_required
from users.models import CustomUser, CoinbaseAccount
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt

def signUp(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        username = request.POST['username']


        if CustomUser.objects.filter(email=email).exists():
            messages.error(request, "Email already in use")
            return redirect('signup')
        
        if password != confirm_password:
            messages.error(request, "Passwords do not match")
            return redirect('signup')
        if not username.strip():
            messages.error(request, "Name is required")
            return redirect('signup')


        
        user = CustomUser.objects.create_user(email=email, password=password, username=username)
        login(request, user)
        return redirect('dashboard-home')
    return render(request, 'users/sign-up.html')

def logIn(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard-home')
        else:
            messages.error(request, "Invalid credentials")
            return redirect('login')
    return render(request, 'users/log-in.html')

@csrf_exempt
@login_required
def connect_coinbase(request):
    state = secrets.token_urlsafe(16)  # prevent CSRF
    request.session['coinbase_oauth_state'] = state

    params = {
        'response_type': 'code',
        'client_id': settings.COINBASE_CLIENT_ID,
        'redirect_uri': settings.COINBASE_REDIRECT_URI,
        'state': state,
        'scope': 'wallet:accounts:read wallet:user:read offline_access',
    }

    base_url = 'https://login.coinbase.com/oauth2/auth'
    url = f"{base_url}?{'&'.join([f'{k}={v}' for k,v in params.items()])}"
    return redirect(url)

@login_required
def coinbase_callback(request):
    error = request.GET.get('error')
    code = request.GET.get('code')
    state = request.GET.get('state')

    if state != request.session.get('coinbase_oauth_state'):
        return redirect('dashboard-home')  # fail silently for now

    token_url = "https://login.coinbase.com/oauth2/token"
    data = {
        'grant_type': 'authorization_code',
        'code': code,
        'client_id': settings.COINBASE_CLIENT_ID,
        'client_secret': settings.COINBASE_CLIENT_SECRET,
        'redirect_uri': settings.COINBASE_REDIRECT_URI
    }

    res = requests.post(token_url, data=data)
    if res.status_code != 200:
        return redirect('dashboard-home')

    token_data = res.json()

    # Save to database
    CoinbaseAccount.objects.update_or_create(
        user=request.user,
        defaults={
            'access_token': token_data['access_token'],
            'refresh_token': token_data.get('refresh_token'),
            'token_expiry': now() + timedelta(seconds=token_data.get('expires_in', 3600)),
            'scope': token_data['scope'],
        }
    )

    return redirect('dashboard-home')

@login_required
def disconnect_coinbase(request):
    try:
        account = CoinbaseAccount.objects.get(user=request.user)
        account.delete()
        messages.success(request, "Coinbase account disconnected.")
    except CoinbaseAccount.DoesNotExist:
        messages.warning(request, "No Coinbase account to disconnect.")
    return redirect('dashboard-home')