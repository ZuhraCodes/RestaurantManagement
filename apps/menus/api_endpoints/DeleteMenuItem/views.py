from apps.menus.models import MenuItem
from rest_framework import generics

class DeleteMenuItemAPIView(generics.DestroyAPIView):
    queryset = MenuItem.objects.all()
    