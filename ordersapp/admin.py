from django.contrib import admin

from ordersapp.models import Order, OrderItem

admin.site.register(OrderItem)
admin.site.register(Order)
