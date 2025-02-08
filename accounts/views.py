from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from . decorators import unauthaticated_user
from django.contrib.auth.decorators import login_required
# Create your views here.
@unauthaticated_user
def sign_up(request):
    if request.method == 'POST':
        try:
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            user_info = User.objects.create_user(username=username, email=email, password=password)
            user_info.save()
            success_msg = 'Successfully created new account'
            messages.success(request, success_msg)
            return redirect('sign_up')
        except Exception as e:
            error_msg = 'Error while creating account'
            messages.error(request, error_msg)
            return redirect('sign_up')
    return render(request, 'sign-up.html')

@unauthaticated_user
def sign_in(request):
    if request.method == 'POST':
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                success_msg = 'Successfully Logged in'
                messages.success(request, success_msg)
                return redirect('index')
        except Exception as e:
            error_msg = 'Error while Logging in'
            messages.error(request, error_msg)
            return redirect('sign_in')
    return render(request, 'sign-in.html')

@login_required(login_url='sign_in')
def sign_out(request):
    logout(request)
    success_msg = 'Successfully Logged out'
    messages.success(request, success_msg)
    return redirect('sign_in')