from rest_framework import serializers
from apps.menus.models import Category

class CreateCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description',]
