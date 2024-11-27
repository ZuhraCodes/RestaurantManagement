from rest_framework.generics import ListAPIView
from .serializers import ViewCartItemSerializer
from rest_framework.response import Response
from rest_framework import status
from apps.orders.models import OrderItem

class ViewCartItemAPIView(ListAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = ViewCartItemSerializer
    
