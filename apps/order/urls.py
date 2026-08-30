from django.urls import path
from .views import *

urlpatterns = [
    path('', order_list, name='order_list'),
    path('checkout/', checkout_view, name='checkout'),
    path('confirmation/<str:order_number>/', confirmation, name='confirmation'),
    path('<str:order_number>/', order_detail, name='order_detail'),
    path('<str:order_number>/cancel/', cancel_order, name='cancel_order'),
]