from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    
    def __str__(self) -> str:
        return self.name
    
class MenuItem(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, related_name="categories", null=True, blank=True)
    quantity = models.IntegerField(default=0)
    available = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return self.name
    