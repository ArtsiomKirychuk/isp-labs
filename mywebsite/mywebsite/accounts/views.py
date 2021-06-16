from django.shortcuts import render
from .models import *

# Create your views here.


def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()
    count_customers = customers.count()
    count_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()
    dict = {'orders': orders, 'customers': customers, 'count_customers': count_customers,
            'count_orders': count_orders, 'delivered': delivered, 'pending': pending}
    return render(request, 'accounts/dashboard.html', dict)


def products(request):
    products = Product.objects.all()
    return render(request, 'accounts/products.html', {'products': products})


def customer(request, primary_key):
    customer = Customer.objects.get(id=primary_key)
    orders = customer.order_set.all()
    count_order = orders.count()
    context = {'customer': customer, 'orders': orders, 'count_order': count_order}
    return render(request, 'accounts/customer.html', context)
