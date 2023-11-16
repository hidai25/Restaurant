from django.contrib import admin
from .models import Order, OrderItem, Product, Category


# Class Used to customize the admin so that the orders details can be seen. Taken from django documentation.
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemInline]


# Registers the different classes in the Admin
admin.site.register(Order, OrderAdmin)
admin.site.register(Product)
admin.site.register(Category)
