from django.conf import settings
from orders.models import Product


class Cart(object):
    # The code for this cart was inspired from https://stackoverflow.com/questions/49027479/have-bugs-in-session-django
    # initialize the cart
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # Initialize an empty cart that would take id's as keys in the dictionary.
            self.session[settings.CART_SESSION_ID] = {}
            cart = {}

        self.cart = cart

    def add(self, product, quantity=1, update_quantity=False, toppings=""):
        # convert to string because django allows strings only
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0, 'price': str(product.price),
                                     'name': product.name, 'category': str(product.category), 'toppings': toppings}

        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    def save(self):
        # make sure the session is updated
        self.session[settings.CART_SESSION_ID] = self.cart

        self.session.modified = True

    def remove(self, product):
        # Function to define remove item from cart
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def get_total_cost(self):
        total_cost = 0
        for product_id in self.cart:
            total_cost += self.cart[product_id]['quantity'] * float(self.cart[product_id]['price'])

        return total_cost

        # Clear the shopping cart
    def clear(self):
        self.session[settings.CART_SESSION_ID] = {}
        self.cart = {}

        self.session.modified = True
