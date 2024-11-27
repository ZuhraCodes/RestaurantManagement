from .serializers import CreateMenuItemSerializer
from apps.menus.models import MenuItem
from rest_framework import generics

class CreateMenuItemAPIView(generics.ListAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = CreateMenuItemSerializer
    