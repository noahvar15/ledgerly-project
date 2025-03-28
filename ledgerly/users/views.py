from django.shortcuts import render

# Create your views here.
def signIn(request):
    return render(request, 'users/sign-in.html', {})

def signUp(request):
    return render(request, 'users/sign-up.html', {})