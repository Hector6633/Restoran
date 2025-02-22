from django.shortcuts import render, redirect
from restaurant.models import Menu
from . models import ContactUs
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def index(request):
    food_items = {
        'items': Menu.objects.all()
    }
    return render(request, 'index.html', food_items)

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == 'POST':
        try:
            customer_name = request.POST.get('name')
            customer_email = request.POST.get('email')
            subject = request.POST.get('subject')
            message = request.POST.get('message')
            customer_feedback = ContactUs.objects.create(customer_name=customer_name, customer_email=customer_email, customer_subject=subject, customer_message=message)
            customer_feedback.save()
            subject = 'Restoran Feedback'
            message = f'Dear {customer_name},\nThank you for your feedback and for choosing Restoran for your food needs.\nTo get started, please visit our website at https://restoran.pythonanywhere.com/ and log in with your new account details & order your favorite dishes.\nWe look forward to serving you!'  
            recipient = customer_email
            send_mail(subject, 
            message, settings.EMAIL_HOST_USER, [recipient], fail_silently=True)
            success_msg = 'Thank you for your feedback'
            messages.success(request, success_msg)
            return redirect('contact')
        except Exception as e:
            error_msg = 'Something went wrong'
            messages.error(request, error_msg)
            return redirect('contact')
    return render(request, 'contact.html')  

