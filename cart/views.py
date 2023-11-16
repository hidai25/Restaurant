from django.shortcuts import render, redirect
from orders.models import Product, Order, OrderItem
from django.template import RequestContext
from .cart import Cart
from django.shortcuts import render
from django.contrib.auth.models import User



def add_to_cart_view(request, product_id):
    # Responsible to add to cart regular items
    cart = Cart(request)
    product = Product.objects.get(pk=product_id)
    cart.add(product=product, quantity=1, update_quantity=False)
    return redirect('cart:cart_detail')


def remove_from_cart_view(request, product_id):
    # Responsible for removing from cart any item
    cart = Cart(request)
    product = Product.objects.get(pk=product_id)
    cart.remove(product=product)
    return redirect('cart:cart_detail')


def cart_detail(request):
    # Responsible for showing the cart
    if request.method == 'GET':
        cart = Cart(request)
        return render(request, 'cart/detail.html', {"cart": cart.cart, "total_cost":cart.get_total_cost })


def checkout_view(request):
    # Responsible for placing an order
    cart = Cart(request)
    user = User.objects.get(pk=request.user.id)
    order = Order.objects.create(user=user, total_price=cart.get_total_cost())
    for product_id, item in cart.cart.items():
        product = Product.objects.get(pk=product_id)
        toppings = request.POST.getlist('checkbox')
        OrderItem.objects.create(order=order, product=product, quantity=item['quantity'], toppings=item['toppings'])
    # Cleans the cart after placing the order
    cart.clear()
    return render(request, 'cart/checkout.html')


def add_pizza_topping_to_cart_view(request):
    # Responsible for adding to cart Pizzas and Toppings items
    product_id = request.POST.get('radio_select')
    toppings = request.POST.getlist('checkbox')
    product = Product.objects.get(pk=product_id)
    cart = Cart(request)
    cart.add(product=product, quantity=1, update_quantity=False, toppings=toppings)
    return redirect('cart:cart_detail')
