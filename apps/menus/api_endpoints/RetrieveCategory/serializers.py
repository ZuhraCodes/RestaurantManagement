from rest_framework import serializers
from apps.menus.models import Category

class RetrieveCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'description',]