from rest_framework import serializers
from apps.menus.models import MenuItem

class RetrieveMenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['name', 'description', 'price', 'category' ,'available']