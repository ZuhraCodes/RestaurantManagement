from rest_framework import serializers
from .utils import get_tokens_for_user
from django.contrib.auth import get_user_model
from rest_framework.exceptions import ValidationError

class LoginUserSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    
    def create(self, validated_data):
        username = validated_data["username"]
        password = validated_data["password"]
        User = get_user_model()
        
        try:
            user = User.objects.get(username=username)
        
            if not user.check_password(password):
                print("password not match")
                raise ValidationError(
                    {
                        "error": "user_not_found",
                        "message": "User with this credentials does not exist"
                    }
                )
            return get_tokens_for_user(user)
            
        except User.DoesNotExist:
            raise ValidationError(
                {
                    "error": "user_not_found",
                    "message": "User with this credentials does not exist"
                }
            )
