
from django.contrib import admin
from django.urls import path

from apps.views import CategoryListCreateAPIView, CategoryRetrieveUpdateDestroyAPIView, ProductListCreateAPIView

urlpatterns = [
        path('category', CategoryListCreateAPIView.as_view() , name = "category-list-create"),
        path('product', ProductListCreateAPIView.as_view() , name = "product-list-create"),
        path('category/<int:pk>', CategoryRetrieveUpdateDestroyAPIView.as_view(), name="category-delete-update-retrieve"),
]


