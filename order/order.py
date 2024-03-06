from django.conf import settings
from product.models import Product

class Order(object):
   def __init__(self, request):
      self.session = request.session
      order = self.session.get(settings.CART_SESSION_ID)

      if not order:
         order = self.session[settings.CART_SESSION_ID] = {}

      self.order = order

   def __iter__(self):
      for p in self.order.keys():
         self.order[str(p)]['product'] = Product.objects.get(pk=p)

      for item in self.order.values():
         item['total_price'] = item['product'].price * item['quantity']

         yield item   

   def __len__(self):
      return sum(item['quantity'] for item in self.order.values())

   def save(self):
      self.session[settings.CART_SESSION_ID] = self.order
      self.session.modified = True

   def add(self,product_id,quantity=1,update_quantity=False):
      product_id = str(product_id)

      if product_id not in self.order:
         self.order[product_id] = {'quantity': 1, 'id': product_id}
      if update_quantity:
         self.order[product_id]['quantity'] += int(quantity)
         if self.order[product_id]['quantity'] == 0:
            self.remove(product_id)
      self.save()         

   def remove(self,product_id):
      if product_id in self.order:
         del self.order[product_id]
         self.save()

   def get_total_cost(self):
      return sum(item['total_price'] for item in self.order.values()) 

   def get_item(self,product_id):
      return self.order[str(product_id)]



