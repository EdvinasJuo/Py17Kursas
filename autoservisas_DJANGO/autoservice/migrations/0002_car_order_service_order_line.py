# Generated by Django 4.2.7 on 2023-11-07 09:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('autoservice', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('license_plate', models.CharField(help_text='Įveskite automobilio valstybinį numerį', max_length=100, verbose_name='Valstybinis_numeris')),
                ('vin_code', models.CharField(help_text='Automobilio VIN numeris (17 simbolių)', max_length=17, verbose_name='VIN_kodas')),
                ('client', models.CharField(help_text='Kliento vardas ir pavardė', max_length=100, verbose_name='Klientas')),
                ('car_model', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='autoservice.car_model')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.CharField(help_text='Data: (YYYY-MM-DD) formatu', max_length=100, verbose_name='Data')),
                ('car_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='autoservice.car')),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Paslaugos pavadinimas', max_length=255, verbose_name='Pavadinimas')),
                ('price', models.FloatField(verbose_name='Kaina')),
            ],
        ),
        migrations.CreateModel(
            name='Order_line',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.CharField(max_length=100, verbose_name='Kiekis')),
                ('order_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='autoservice.order')),
                ('service_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='autoservice.service')),
            ],
        ),
    ]