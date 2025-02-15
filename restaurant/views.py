from django.shortcuts import render, redirect
from . models import Booking_table
from django.contrib import messages
from django.contrib.auth.decorators import login_required
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
    return render(request, 'menu.html')