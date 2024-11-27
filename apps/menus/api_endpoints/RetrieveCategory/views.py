from .serializers import RetrieveCategorySerializer
from apps.menus.models import Category
from rest_framework import generics

class RetrieveCategoryAPIView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = RetrieveCategorySerializer
    