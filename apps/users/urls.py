from django.urls import path
from apps.users import api_endpoints 
from apps.users.api_endpoints.LoginUser.views import UserLoginAPIView

urlpatterns = [
    path('login/', UserLoginAPIView.as_view(), name='login')
]