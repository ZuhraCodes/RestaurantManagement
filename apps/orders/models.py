from django.db import models
from apps.menus.models import MenuItem
from apps.users.models import User



class Order(models.Model):
    
    class OrderStatus(models.TextChoices):
        PENDING = 'pending', 'New Order'
        COMPLETED = 'completed', 'Completed'
        CANCELLED = 'cancelled', 'Cancelled'
    
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    status = models.CharField(OrderStatus.choices, default=OrderStatus.PENDING, max_length=16 )
    total_price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

class OrderItem(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE, related_name="order_menu_items")
    user = models.ForeignKey("users.User", on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.IntegerField()
    price = models.IntegerField()
    status = models.CharField(choices=Order.OrderStatus.choices, default=Order.OrderStatus.PENDING, max_length=16)
    
    