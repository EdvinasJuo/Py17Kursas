from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Order, Driver, Product, Route, Vehicle, Warehouse


# Create your views here.

#Kuriamos funkcijos kurios bus atvaizduojamos urls.py
def index(request):

    orders_count = Order.objects.all().count()
    drivers_count = Driver.objects.all().count()

    context = {
        'orders_count': orders_count, # KEY IR VALUE kuris ateina is 12 eilutes.
        'drivers_count': drivers_count,
    }

    # nurodom i kur paduodam sita funkcija ir context. siuo metu i index.html faila
    return render(request, 'index.html', context=context)

def drivers(request):

    all_drivers = Driver.objects.all()
    context = {
        'all_drivers': all_drivers
    }

    #PAIESKOS LAUKELIS
    query = request.GET.get('q')
    if query:
        search_drivers = Driver.objects.filter(
            Q(name__icontains=query) |
            Q(driver_number__icontains=query) |
            Q(email__icontains=query)
        )
        context['all_drivers'] = search_drivers

    return render(request, 'drivers.html', context=context)

def driver(request, driver_id):
    single_driver = get_object_or_404(Driver, pk=driver_id)
    return render(request, 'driver.html', {'driver': single_driver})

def orders(request):

    all_orders = Order.objects.all()
    context = {
        'all_orders': all_orders
    }

    # PAIESKOS LAUKELIS
    query = request.GET.get('q')
    if query:
        search_orders = Order.objects.filter(
            Q(customer__name__icontains=query) |
            Q(status__icontains=query) |
            Q(order_date__icontains=query)
        )
        context['all_orders'] = search_orders

    return render(request, 'orders.html', context=context)


def products(request):

    all_products = Product.objects.all()
    context = {
        'all_products': all_products
    }

    # PAIESKOS LAUKELIS
    query = request.GET.get('q')
    if query:
        search_products = Product.objects.filter(
            Q(name__icontains=query) |
            Q(unit_price__icontains=query)
        )
        context['all_products'] = search_products

    return render(request, 'products.html', context=context)


def routes(request):

    all_routes = Route.objects.all()
    context = {
        'all_routes': all_routes
    }

    # PAIESKOS LAUKELIS
    query = request.GET.get('q')
    if query:
        search_routes = Route.objects.filter(
            Q(order__customer__name__icontains=query) |
            Q(vehicle__plate_number__icontains=query)
        )
        context['all_routes'] = search_routes

    return render(request, 'routes.html', context=context)

def route(request, route_id):
    single_route = get_object_or_404(Route, pk=route_id)
    return render(request, 'route.html', {'route': single_route})

def vehicles(request):
    all_vehicles = Vehicle.objects.all()
    context = {
        'all_vehicles': all_vehicles
    }

    # PAIESKOS LAUKELIS
    query = request.GET.get('q')
    if query:
        search_vehicles = Vehicle.objects.filter(
            Q(type__icontains=query) |
            Q(plate_number__icontains=query)
        )
        context['all_vehicles'] = search_vehicles

    return render(request, 'vehicles.html', context=context)

def warehouses(request):
    all_warehouses = Warehouse.objects.all()
    context = {
        'all_warehouses': all_warehouses
    }

    # PAIESKOS LAUKELIS
    query = request.GET.get('q')
    if query:
        search_warehouses = Warehouse.objects.filter(
            Q(name__icontains=query) |
            Q(location__icontains=query)
        )
        context['all_warehouses'] = search_warehouses

    return render(request, 'warehouses.html', context=context)