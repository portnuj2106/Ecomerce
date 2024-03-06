
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from order.views import add_to_order,order,hx_add_to_order,update_order,checkout_page

urlpatterns = [
    path('', include('core.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('products/', include('product.urls')),
    path('order/', order, name="order"),
    path('order/checkout_page/', checkout_page, name='checkout_page'),
    path('add_to_order/<int:product_id>/',add_to_order,name="add_to_order"),
    path('update_order/<int:product_id>/<str:action>/', update_order, name="update_order"),
    path('hx_add_to_order/', hx_add_to_order, name="hx_add_to_order"),
    path('checkout/', include('checkout.urls')),
    path('admin/', admin.site.urls),
]
