from django.shortcuts import render, redirect
from . models import Booking_table
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from . models import Menu
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
@login_required(login_url='sign_in')
def book_a_table(request):
    if request.method == 'POST':
        try:
            customer_name = request.POST.get('name')
            customer_email = request.POST.get('email')
            date_time = request.POST.get('date&time')
            special_req = request.POST.get('special_req')
            booking_data = Booking_table.objects.create(customer_name=customer_name, customer_email=customer_email, 
            date_time=date_time, special_req=special_req)
            subject = 'Restoran Table Booking'
            message = f'Dear {customer_name},\nYour booking is successfully received with Restoran.\n Here is your booking details:\n\tCustomer Name: {customer_name}\n\tCustomer Email:{customer_email}\n\tBooking Date & Time: {date_time}\nPlease keep this email for your records and do not forward or share any other person.To get started, please visit our website at https://restoran.pythonanywhere.com/ and log in with your new account details & order your favorite dishes.\nWe look forward to serving you!'  
            recipient = customer_email
            send_mail(subject, 
            message, settings.EMAIL_HOST_USER, [recipient], fail_silently=True)
            success_msg = 'Your booking is successfully received'
            messages.success(request, success_msg)  
            booking_data.save()
        except Exception as e:
            error_msg ='Server error occurred try again later'  
            messages.error(request, error_msg)
            return redirect('book_a_table')                                   
    return render(request, 'booking.html')

def service(request):
    return render(request, 'service.html')

def menu(request):
    menu_items = {
        'items' : Menu.objects.all()
    }
    return render(request, 'menu.html', menu_items)