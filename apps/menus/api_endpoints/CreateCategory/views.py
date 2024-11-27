from .serializers import CreateCategorySerializer
from apps.menus.models import Category
from rest_framework import generics

class CreateCategoryAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CreateCategorySerializer
    