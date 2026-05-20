from django.shortcuts import render, redirect
from django.contrib.auth import login,logout,authenticate
from .models import User
from django.contrib.auth.decorators import login_required
from bookings.models import Booking
from services.models import Service
from collections import defaultdict

def register(request):
    error = None
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        is_seller = request.POST.get('is_seller') == 'on'

        if User.objects.filter(username=username).exists():
            error = "Username already exists"
        else:

            user = User.objects.create_user(
                username=username,
                password=password,
                is_seller=is_seller
            )

            login(request, user)
            return redirect('/')

    return render(request, 'accounts/register.html',{'error':error})

def user_login(request):
    error = None
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/accounts/dashboard/')

        else:
            error = "Invalid username or password"

    return render(request, 'accounts/login.html',{'error':error})

def user_logout(request):
    logout(request)
    return redirect('/')

@login_required
def buyer_dashboard(request):
    return render(request, 'accounts/buyer_dashboard.html')

@login_required
def seller_dashboard(request):
    return render(request, 'accounts/seller_dashboard.html')
    
def dashboard_redirect(request):
    if request.user.is_seller:
        return redirect('/accounts/seller/')
    else:
        return redirect('/accounts/buyer/')