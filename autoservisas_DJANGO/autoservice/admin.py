from django.contrib import admin
from .models import Car_model, Car, Order, Service, Order_line, CarReview, Profilis


class CarAdmin(admin.ModelAdmin):
    list_display = ('car_model', 'license_plate', 'vin_code', 'client')
    list_filter = ('car_model__make','client')
    search_fields = ('license_plate', 'vin_code')
class CarModelAdmin(admin.ModelAdmin):
    list_display = ('make', 'model')

class OrderLineAdmin(admin.ModelAdmin):
    list_display = ('service', 'order', 'quantity')
    list_editable = ('order', 'quantity')


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'formatted_price')

    def formatted_price(self, obj):
        return f'{obj.price} €'

    formatted_price.short_description = 'Kaina (€)'

class OrderLinesInLine(admin.TabularInline):
    model = Order_line
    extra = 0

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id','car_make','car_model', 'reader','due_back', 'data')
    inlines = [OrderLinesInLine]
    def car_make(self, obj):
        return obj.car.car_model.make

    def car_model(self, obj):
        return obj.car.car_model.model

    def car_id(self,obj):
        return obj.car.car_model.id

    car_model.short_description = "Modelis"
    car_make.short_description = "Markė"
    car_id.short_description = "Id"


class CarReviewAdmin(admin.ModelAdmin):
    list_display = ('car', 'date_created', 'reviewer', 'content')

# Register your models here.
admin.site.register(Car_model, CarModelAdmin)
admin.site.register(Car, CarAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Order_line, OrderLineAdmin)
admin.site.register(CarReview, CarReviewAdmin)
admin.site.register(Profilis)