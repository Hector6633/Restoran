from django.db import models

# Create your models here.
class Booking_table(models.Model):
    customer_name = models.CharField(max_length=50)
    customer_email = models.EmailField()
    date_time = models.CharField(max_length=50)
    no_of_people = models.CharField(max_length=50)
    ordered_item = models.CharField(max_length=50)
    beverage = models.CharField(max_length=50)
    special_req = models.TextField()
    
    def __str__(self):
        return self.customer_name
    
class Menu(models.Model):
    item_name = models.CharField(max_length=100)
    item_price = models.CharField(max_length=100)
    item_des = models.CharField(max_length=100)
    item_img = models.ImageField(upload_to='static/img/menu')
    
    def __str__(self):
        return self.item_name  
    
class Beverages(models.Model):
    product_name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.product_name
      
    