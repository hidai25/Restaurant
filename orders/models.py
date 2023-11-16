from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse



class Category(models.Model):
    # Defines the field of different categories
    name = models.CharField(max_length=50, db_index=True)

    def __str__(self):
        return f"{self.name}"


class Product(models.Model):
    # Defines the fields of the food products in each cartegory
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, db_index=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.category} {self.name} {self.price}"


class Order(models.Model):
    # Define the fields of each order
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.created} {self.user} {self.total_price}"


class OrderItem(models.Model):
    # Defines the fields of an order items
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    toppings = models.CharField(max_length=50, db_index=True, blank=True, null=True)

    def __str__(self):
        return f"{self.order} {self.product} {self.toppings}  {self.quantity}"
