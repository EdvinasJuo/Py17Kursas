# Generated by Django 4.2.7 on 2023-11-08 07:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('autoservice', '0003_rename_car_id_order_car_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='car',
            options={'verbose_name': 'Automobilis', 'verbose_name_plural': 'Automobiliai'},
        ),
        migrations.AlterModelOptions(
            name='car_model',
            options={'verbose_name': 'Automobilio modelis', 'verbose_name_plural': 'Automobilių modeliai'},
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'Eilė', 'verbose_name_plural': 'Eilės'},
        ),
        migrations.AlterModelOptions(
            name='order_line',
            options={'verbose_name': 'Užsakymo eilė', 'verbose_name_plural': 'Užsakymo eilės'},
        ),
        migrations.AlterModelOptions(
            name='service',
            options={'verbose_name': 'Paslauga', 'verbose_name_plural': 'Paslaugos'},
        ),
    ]
