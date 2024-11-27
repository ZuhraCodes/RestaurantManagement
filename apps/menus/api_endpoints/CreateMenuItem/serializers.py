from rest_framework import serializers
from apps.menus.models import MenuItem

class CreateMenuItemSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source="category.name")
    class Meta:
        model = MenuItem
        fields = ['id', 'name', 'description', 'price', 'category', 'available',]
