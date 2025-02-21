from django.shortcuts import render, redirect
from restaurant.models import Menu
from . models import ContactUs
from django.contrib import messages

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
            success_msg = 'Thank you for your feedback'
            messages.success(request, success_msg)
            return redirect('contact')
        except Exception as e:
            error_msg = 'Something went wrong'
            messages.error(request, error_msg)
            return redirect('contact')
    return render(request, 'contact.html')  

