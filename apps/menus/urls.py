from django.urls import path
from apps.menus import api_endpoints

urlpatterns = [
    path('create/category/', api_endpoints.CreateCategoryAPIView.as_view(), name="create-category"),
    path('create/menuitem/', api_endpoints.CreateMenuItemAPIView.as_view(), name="create-menu-item"),
    path('category/detail/<int:pk>/', api_endpoints.RetrieveCategoryAPIView.as_view(), name="category-detail"),
    path('menuitem/detail/<int:pk>/', api_endpoints.RetrieveMenuItemAPIView.as_view(), name="menu-item-detail"),
    path('update/category/<int:pk>/', api_endpoints.UpdateCategoryAPIView.as_view(), name="update-category"),
    path('update/menuitem/<int:pk>/', api_endpoints.UpdateMenuItemAPIView.as_view(), name="update-menu-item"),
    path('delete/category/<int:pk>/', api_endpoints.DeleteCategoryAPIView.as_view(), name="delete-category"),
    path('delete/menuitem/<int:pk>/', api_endpoints.DeleteMenuItemAPIView.as_view(), name="delete-menu-item"),
]