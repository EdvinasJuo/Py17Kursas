import uuid

from django.db import models
from django import forms
from django.urls import reverse
from django.utils import timezone
from datetime import datetime

# Create your models here.
class Customer(models.Model):
    name = models.CharField('Vardas Pavarde', max_length=80, help_text='Įveskite užsakovo vardą ir pavardę')
    email = models.CharField('El.Paštas', max_length=100, unique=True, help_text='Įveskite el. paštą')
    location = models.CharField('Adresas', max_length=100, help_text='Įveskite adresą')
    phone_number = models.CharField('Tel.Nr', max_length=25, help_text='Įveskite Tel.Nr.')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """Nurodo visa customer informacija"""
        return reverse('customer-detail', args=[self.email])


class Vehicle(models.Model):
    type = models.CharField('Transporto tipas', max_length=80, help_text='Įveskite transporto priemonės tipą')
    plate_number = models.CharField('Valstybinis nr.', max_length=20, help_text='Įveskite valstybinį numerį')

    VEHICLE_STATUS = (
        ('a', 'Administruojama'),
        ('l', 'Laisva'),
        ('u', 'Užimta')
    )

    status = models.CharField(
        max_length=1,
        choices=VEHICLE_STATUS,
        blank=True,
        default='a',
        help_text='Statusas',
    )

    # Gaunamas value is ORDER_STATUS dictionary
    def get_status_display_value(self):
        for code, display_value in self.VEHICLE_STATUS:
            if code == self.status:
                return display_value
        return self.status  # Grazinamas kodas jeigu nerasta rezultatu

    def __str__(self):
        return f'{self.plate_number}'


class Driver(models.Model):
    name = models.CharField('Vardas Pavarde', max_length=80, help_text='Įveskite vairuotojo vardą ir pavardę')
    driver_number = models.CharField('Darbuotojo numeris', max_length=20, help_text='Įveskite darbuotojo numerį')
    phone_number = models.CharField('Tel.Nr', max_length=25, help_text='Įveskite Tel.Nr.')
    email = models.CharField('El.Paštas', max_length=100, unique=True,  help_text='Įveskite el. paštą')
    vehicle = models.ForeignKey('Vehicle', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.name}'



class Product(models.Model):
    name = models.CharField('Produktas', max_length=50, help_text='Įveskite produkto pavadinimą')
    unit_price = models.FloatField('Vieneto kaina', help_text='Įveskite vieneto kainą')
    #Galimybe prideti quantity_in_stock

    def __str__(self):
        return f'{self.name} - {self.unit_price}€'


class Warehouse(models.Model):
    name = models.CharField('Sandelys', max_length=50, help_text='Įveskite sandėlio pavadinimą')
    location = models.CharField('Lokacija', max_length=100, help_text='Įveskite sandėlio lokaciją')

    def __str__(self):
        return f'{self.name} - {self.location}'


class Order(models.Model):
    customer = models.ForeignKey('Customer', on_delete=models.SET_NULL, null=True)
    order_date = models.DateField()

    def save(self, *args, **kwargs):
        if not self.order_date:
            self.order_date = timezone.now().date()
        super().save(*args, **kwargs)

    ORDER_STATUS = (
        ('a', 'Administruojama'),
        ('v', 'Vykdomas'),
        ('b', 'Baigtas'),
        ('a', 'Atšauktas'),
    )

    status = models.CharField(
        max_length=1,
        choices=ORDER_STATUS,
        blank=True,
        default='a',
        help_text='Statusas',
    )

    driver = models.ForeignKey('Driver', on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField('Kiekis', help_text='Įveskite produkto kiekį', default=0, null=False)
    warehouse = models.ForeignKey('Warehouse', on_delete=models.SET_NULL, null=True)

    #Gaunamas value is ORDER_STATUS dictionary
    def get_status_display_value(self):
        for code, display_value in self.ORDER_STATUS:
            if code == self.status:
                return display_value
        return self.status #Grazinamas kodas jeigu nerasta rezultatu

    """Gaunama bendra produkto suma"""
    def get_total_price(self):
        if self.product and self.quantity:
            return self.product.unit_price * self.quantity
        else:
            return 0.0

    def __str__(self):
        return (f'{self.customer}')


class Route(models.Model):
    order = models.ForeignKey('Order', on_delete=models.SET_NULL, null=True)
    vehicle = models.ForeignKey('Vehicle', on_delete=models.SET_NULL, null=True)
    departure = models.DateField(help_text='Įveskite išvykimo datą')
    arrival = models.DateField(help_text='Įveskite atvykimo datą')
    warehouse = models.ForeignKey('Warehouse', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return (f'ID: {self.order.id}. Valstybinis nr: {self.vehicle.plate_number}. '
                f'Išvykimo data: {self.departure}. Atvykimo data: {self.arrival} Išvyksta iš {self.warehouse} '
                f'Vyksta į {self.order.customer.location}')

class RouteForm(forms.ModelForm):
    class Meta:
        model = Route
        fields = '__all__'
        widgets = {
            'departure': forms.DateInput(attrs={'type': 'date'}),
            'arrival': forms.DateInput(attrs={'type': 'date'})
        }
