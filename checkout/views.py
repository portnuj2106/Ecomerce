from django.shortcuts import render,redirect
from .models import Checkout,CheckoutItem
from order.order import Order

def start_checkout(request):
   order = Order(request)
   if request.method == 'POST':
      name = request.POST.get('name')
      email = request.POST.get('email')
      phone = request.POST.get('phone')

      checkout = Checkout.objects.create(user=request.user, name=name, email=email, phone=phone)

      for item in order:
         product = item['product']
         quantity = int(item['quantity'])
         price = product.price * quantity

         item = CheckoutItem.objects.create(checkout=checkout, product=product,price=price, quantity=quantity)

      return redirect('order')
   return redirect('order')