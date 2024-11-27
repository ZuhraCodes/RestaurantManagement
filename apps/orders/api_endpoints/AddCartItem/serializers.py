from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from apps.menus.models import MenuItem

class AddCartItemSerializer(serializers.Serializer):
    meal_id = serializers.IntegerField()
    quantity = serializers.IntegerField()
    
    def create(self, validated_data):
        meal_id = validated_data['meal_id']
        quantity = validated_data['quantity']
        user = self.context["request"].user
        
        try:
            meal = MenuItem.objects.get(id=meal_id)
            
            if quantity > meal.quantity:
                raise ValidationError({"error": "We don't have enough quantity"})
                
            MenuItem.objects.update_or_create(
                meal=meal,
                user=user,
                defaults={
                    "quantity": quantity
                }
            )
            
            return {"message": "Created successfully"}
        
        except MenuItem.DoesNotExist:
            raise ValidationError({"error": "Meal not found"})