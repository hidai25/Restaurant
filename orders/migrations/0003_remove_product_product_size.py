# Generated by Django 2.0.3 on 2018-04-11 20:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_product_product_size'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='product_size',
        ),
    ]