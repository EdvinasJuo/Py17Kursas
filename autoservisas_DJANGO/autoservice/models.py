from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import date
from tinymce.models import HTMLField
from PIL import Image

# Create your models here.
class Car_model(models.Model):
    make = models.CharField('Markė', max_length=100, help_text='Įveskite automobilio markę')
    model = models.CharField('Modelis', max_length=100, help_text='Įveskite automobilio modelį')

    def __str__(self):
        return f'{self.make} {self.model}'

    class Meta:
        verbose_name = "Automobilio modelis"
        verbose_name_plural = "Automobilių modeliai"

    def display_car_models(self):
        return ', '.join(str(car_model) for car_model in self.car_model.all()[:2])

    display_car_models.short_description = "Automobilių modeliai"

class Car(models.Model):
    license_plate = models.CharField('Valstybinis_numeris',max_length=100, help_text='Įveskite automobilio valstybinį numerį')
    car_model = models.ForeignKey('Car_model', on_delete=models.SET_NULL, null=True)
    vin_code = models.CharField('VIN_kodas', max_length=17, help_text='Automobilio VIN numeris (17 simbolių)')
    client = models.CharField('Klientas', max_length=100, help_text='Kliento vardas ir pavardė')
    cover = models.ImageField('Viršelis', upload_to='covers', null=True)

    def __str__(self):
        return f'{self.car_model} - {self.license_plate}'

    def get_absolute_url(self):
        """Nurodo visa automobilio informacija"""
        return reverse('car-detail', args=[self.license_plate])

    class Meta:
        verbose_name = "Automobilis"
        verbose_name_plural = "Automobiliai"

    def display_car_models(self):
        return ', '.join(str(car) for car in self.car_model.all()[:4])

    display_car_models.short_description = "Automobiliai"

class Order(models.Model):
    data = models.DateField('Data', help_text='Data: (YYYY-MM-DD) formatu')
    car = models.ForeignKey('Car', on_delete=models.SET_NULL, null=True)
    reader = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    due_back = models.DateField('Due Back', null=True, blank=True)

    @property
    def is_overdue(self):
        if self.due_back and date.today() > self.due_back:
            return True
        return False

    ORDER_STATUS = (
        ('v', 'Vykdomas'),
        ('p', 'Pabaigtas'),
        ('n', 'Nepradėtas')
    )

    status = models.CharField(
        max_length=1,
        choices=ORDER_STATUS,
        blank=True,
        default='n',
        help_text='Statusas'
    )

    def __str__(self):
        return f'Uzsakymo ID: {self.id} Data: {self.data}. Valstybinis numeris: {self.car}'

    def get_absolute_url(self):
        """Nurodo konkretaus aprašymo galinį adresą"""
        return reverse('order-detail', args=[str(self.id)])

    class Meta:
        verbose_name = "Užsakymas"
        verbose_name_plural = "Užsakymai"

    def display_order_models(self):
        return ', '.join(str(order) for order in self.order.all()[:2])

    display_order_models.short_description = "Užsakymai"

class Service(models.Model):
    name = models.CharField('Pavadinimas', max_length=255, help_text='Paslaugos pavadinimas')
    price = models.FloatField('Kaina')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Paslauga"
        verbose_name_plural = "Paslaugos"

    def display_service_models(self):
        return ', '.join(str(service) for service in self.service.all()[:2])

    display_service_models.short_description = "Paslaugos"

class Order_line(models.Model):
    service = models.ForeignKey('Service', on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey('Order', on_delete=models.SET_NULL, null=True)
    quantity = models.CharField('Kiekis', max_length=100)



    def __str__(self):
        return f'Paslauga: {self.service}'

    class Meta:
        verbose_name = "Užsakymo eilė"
        verbose_name_plural = "Užsakymo eilės"

    def display_order_lines_models(self):
        return ', '.join(str(order_line) for order_line in self.order_line.all()[:4])

    display_order_lines_models.short_description = "Užsakymų eilės"

class CarReview(models.Model):
    car = models.ForeignKey('Car', on_delete=models.SET_NULL, null=True, blank=True)
    reviewer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    content = models.TextField('Atsiliepimas', max_length=2000)

    class Meta:
        verbose_name = "Atsiliepimas"
        verbose_name_plural = 'Atsiliepimai'
        ordering = ['-date_created']

class Profilis(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nuotrauka = models.ImageField(default="default.png", upload_to="profile_pics")

    def __str__(self):
        return f"{self.user.username} profilis"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.nuotrauka.path)
        if img.height > 100 or img.width > 100:
            output_size = (100, 100)
            img.thumbnail(output_size)
            img.save(self.nuotrauka.path)