# Generated by Django 2.0.3 on 2018-04-17 19:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0011_orderitem_toppings'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PizzaToppings',
        ),
    ]
