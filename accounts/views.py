from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from . decorators import unauthaticated_user
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
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
            subject = 'Restoran Account'
            message = f'Dear {username},\nCongratulations on creating your new account with Restoran. Thank you for choosing us for your food needs.\nHere are your account details:\n\tUsername: {username}\n\tE-mail:{email}\nPlease keep this email for your records and do not forward or share any other person. To get started, please visit our website at https://restoran.pythonanywhere.com/ and log in with your new account details & order your favorite dishes.\nWe look forward to serving you!'  
            recipient = email
            send_mail(subject, 
            message, settings.EMAIL_HOST_USER, [recipient], fail_silently=True)
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
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                success_msg = 'Successfully Logged in'
                messages.success(request, success_msg)
                return redirect('index')
            else:
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