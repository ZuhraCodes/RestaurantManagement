from django.urls import path
from apps.orders import api_endpoints

urlpatterns = [
    path("add/", api_endpoints.AddCartItemAPIView.as_view(), name="cart"),
    path("view/", api_endpoints.ViewCartItemAPIView.as_view(), name="view-order-item")
]