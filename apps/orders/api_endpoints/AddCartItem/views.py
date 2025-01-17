from rest_framework.generics import GenericAPIView
from .serializers import AddCartItemSerializer
from rest_framework.response import Response
from rest_framework import status

class AddCartItemAPIView(GenericAPIView):
    serializer_class = AddCartItemSerializer
    
    def post(self, request, *args, **kwargs):
        data = self.serializer_class(data=request.data, context={"request": request})
        if data.is_valid():
            response = data.save()
            return Response(response)
        
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)
    
__all__ = ['AddCartItemAPIView']