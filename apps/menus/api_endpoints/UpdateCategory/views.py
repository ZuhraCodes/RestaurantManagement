from .serializers import UpdateCategorySerializer
from apps.menus.models import Category
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

class UpdateCategoryAPIView(generics.UpdateAPIView):
    http_method_names = ['patch']
    queryset = Category.objects.all()
    serializer_class = UpdateCategorySerializer
    permission_classes = [IsAuthenticated]
    