from django.urls import path

from . import views

# ATVAIZDUOJA IS VIEWS FAILO NURODZIOJ NAME = ''
# PIRMOSE KABUTESE NURODOMAS PATH PAVADINIMAS pvz http://127.0.0.1:8000/test
urlpatterns = [
    path('', views.index, name='index'),
    path('drivers/', views.drivers, name='drivers'),
    path('drivers/<int:driver_id>', views.driver, name='driver'),
    path('orders/', views.orders, name='orders'),
    path('produtcs/', views.products, name='products'),
    path('routes/', views.routes, name='routes'),
    path('routes/<int:route_id>', views.route, name='route'),
    path('vehicles/', views.vehicles, name='vehicles'),
    path('warehouses/', views.warehouses, name='warehouses'),
]