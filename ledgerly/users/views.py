from django.shortcuts import render, redirect
from users.models import CustomUser
from django.contrib.auth import login, authenticate
from django.contrib import messages

def signUp(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']


        if CustomUser.objects.filter(email=email).exists():
            messages.error(request, "Email already in use")
            return redirect('signup')
        
        if password != confirm_password:
            messages.error(request, "Passwords do not match")
            return redirect('signup')

        
        user = CustomUser.objects.create_user(email=email, password=password)
        login(request, user)
        return redirect('dashboard-home')
    return render(request, 'users/sign-up.html')

def signIn(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard-home')
        else:
            messages.error(request, "Invalid credentials")
            return redirect('signin')
    return render(request, 'users/sign-in.html')