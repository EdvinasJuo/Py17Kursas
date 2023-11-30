# Generated by Django 4.2.7 on 2023-11-07 09:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('autoservice', '0002_car_order_service_order_line'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='car_id',
            new_name='car',
        ),
        migrations.RenameField(
            model_name='order_line',
            old_name='order_id',
            new_name='order',
        ),
        migrations.RenameField(
            model_name='order_line',
            old_name='service_id',
            new_name='service',
        ),
    ]