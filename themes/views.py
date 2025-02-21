from django.shortcuts import render
from restaurant.models import Menu
# Create your views here.
def index(request):
    food_items = {
        'items': Menu.objects.all()
    }
    return render(request, 'index.html', food_items)

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')  

