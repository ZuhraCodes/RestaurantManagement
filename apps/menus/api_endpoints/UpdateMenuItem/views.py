from .serializers import UpdateMenuItemSerializer
from apps.menus.models import MenuItem
from rest_framework import generics

class UpdateMenuItemAPIView(generics.UpdateAPIView):
    http_method_names = ['patch']
    queryset = MenuItem.objects.all()
    serializer_class = UpdateMenuItemSerializer
    