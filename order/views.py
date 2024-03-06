from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .order import Order
from product.models import Product


@login_required
def add_to_order(request, product_id):
    order = Order(request)
    order.add(product_id)

    return render(request,'order/add_to_order.html')

@login_required
def checkout_page(request):
    return render(request, 'order/checkout_page.html')


@login_required
def order(request):
    order = Order(request)

    print(order)
    for item in order:
        print(item)

    return render(request,'order/order_summary.html')

def update_order(request, product_id, action):
    order = Order(request)

    if action == 'increment':
        order.add(product_id,1,True)
    else:
        order.add(product_id,-1,True)   

    product = Product.objects.get(pk=product_id)
    quantity = order.get_item(product_id)['quantity']


    item = {
        'product': {
            'id':product.id,
            'name':product.name,
            'description':product.description,
            'price':product.price,
        },
        'total_price': (quantity * product.price),
        'quantity':quantity,
    }   

    response = render(request, 'order/partials/order_item.html', {'item': item})
    response['HX-Trigger'] = 'update_add_to_order'

    return response

def hx_add_to_order(request):
    return render(request,'order/add_to_order.html')



	