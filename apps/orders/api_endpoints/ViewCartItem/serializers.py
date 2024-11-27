from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from apps.orders.models import OrderItem
from apps.users.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name', )
    
    

class ViewCartItemSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = OrderItem
        fields = ['id', 'user' ,'menu_item', 'price', 'quantity', 'status', ]