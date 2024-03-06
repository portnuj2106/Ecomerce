from django.db import models

from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    created_by = models.ForeignKey(User, related_name='products', on_delete=models.CASCADE,default=1)
    def __str__(self):
        return self.name
    

# class Order(models.Model):
#     name = models.CharField(max_length=255)
#     description = models.TextField(blank=True, null=True)
#     price = models.FloatField()
        
#     def __str__(self):
#         return self.name
