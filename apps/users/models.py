from django.db import models
from django.contrib.auth.models import AbstractUser

class User(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=16)
    is_staff = models.BooleanField(default=False)
    
class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="cart_items")
    menu_items = models.ForeignKey("menus.MenuItem", on_delete=models.CASCADE, related_name="menu_items")
    quantity = models.IntegerField()
    
    