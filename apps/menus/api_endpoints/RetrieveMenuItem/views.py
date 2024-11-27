from .serializers import RetrieveMenuItemSerializer
from apps.menus.models import Category
from rest_framework import generics

class RetrieveMenuItemAPIView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = RetrieveMenuItemSerializer
    