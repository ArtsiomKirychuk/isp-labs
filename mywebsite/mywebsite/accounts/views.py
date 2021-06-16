from django.shortcuts import render, redirect
from .models import *
from.forms import OrderForm

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


def createOrder(request):
    form = OrderForm()
    if request.method == 'POST':
        print('Printing POST', request.POST)
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    dict = {'form': form}
    return render(request, 'accounts/order_form.html', dict)


def updateOrder(request, primary_key):
    order = Order.objects.get(id=primary_key)
    form = OrderForm(instance=order)
    if request.method == 'POST':
        print('Printing POST', request.POST)
        form = OrderForm(request.POST,instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render (request, 'accounts/order_form.html', context)

def delete_order(request, primary_key):
    order = Order.objects.get(id=primary_key)
    if request.method =='POST':
        order.delete()
        return redirect('/')
    context = {'item': order}
    return render(request, 'accounts/delete.html', context)

