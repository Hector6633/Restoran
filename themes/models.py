from django.db import models

# Create your models here.
class ContactUs(models.Model):
    customer_name = models.CharField(max_length=50)
    customer_email = models.EmailField()
    customer_subject = models.CharField(max_length=50)
    customer_message = models.TextField()
    
    def __str__(self):
        return self.customer_name