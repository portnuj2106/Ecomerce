from django.urls import path

from .views import start_checkout

urlpatterns = [
   path('start_checkout/', start_checkout, name='start_checkout'),
]