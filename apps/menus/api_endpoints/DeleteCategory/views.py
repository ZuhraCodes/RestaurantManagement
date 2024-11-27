from apps.menus.models import Category
from rest_framework import generics

class DeleteCategoryAPIView(generics.DestroyAPIView):
    queryset = Category.objects.all()
    