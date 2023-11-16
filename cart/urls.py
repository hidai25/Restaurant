from django.urls import *
from django.urls import path
from orders.models import Product
from . import views


app_name = 'cart'
urlpatterns = [
    # All the urls related to the cart
    path("cart", views.cart_detail, name="cart_detail"),
    path("add_to_cart/<product_id>", views.add_to_cart_view, name="add_to_cart"),
    path("add_pizza_topping_to_cart_view", views.add_pizza_topping_to_cart_view, name="add_pizza_topping_to_cart_view"),
    path("remove_from_cart/<product_id>", views.remove_from_cart_view, name="remove_from_cart"),
    path("Checkout", views.checkout_view, name="checkout"),
]
