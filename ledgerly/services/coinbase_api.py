import requests
from users.models import CoinbaseAccount
from django.utils.timezone import now

def is_coinbase_connected(user):
    try:
        account = CoinbaseAccount.objects.get(user=user)
        if account.token_expiry < now():
            return False  # Token expired (you can later refresh it here)
        
        headers = {
            'Authorization': f'Bearer {account.access_token}',
        }
        res = requests.get('https://api.coinbase.com/v2/user', headers=headers)
        return res.status_code == 200
    except CoinbaseAccount.DoesNotExist:
        return False
