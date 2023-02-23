from django.contrib import admin

from .models import CustomerShipping, OrderDetail

admin.site.register(CustomerShipping)
admin.site.register(OrderDetail)
