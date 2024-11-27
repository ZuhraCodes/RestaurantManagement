from django.contrib import admin
from .models import Order, OrderItem

admin.site.register(Order)

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('menu_item', 'quantity', 'price')
    fields = ('menu_item', 'quantity', 'price', 'status') 
