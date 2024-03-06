from django.db import models
from django.contrib.auth.models import User
from product.models import Product


class Checkout(models.Model):
   user = models.ForeignKey(User, related_name='checkouts', blank=True, null=True, on_delete=models.CASCADE)
   name = models.CharField(max_length=255)
   email = models.CharField(max_length=255)
   phone = models.CharField(max_length=255)
   created_at = models.DateTimeField(auto_now_add=True)

class CheckoutItem(models.Model):
   checkout = models.ForeignKey(Checkout, related_name='items', on_delete=models.CASCADE) 
   product = models.ForeignKey(Product, related_name='items', on_delete=models.CASCADE) 
   price = models.IntegerField()
   quantity = models.IntegerField(default=1) 

