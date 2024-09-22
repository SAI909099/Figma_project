from django.shortcuts import render
from drf_spectacular.utils import extend_schema
from rest_framework.generics import ListCreateAPIView, DestroyAPIView, RetrieveUpdateDestroyAPIView

from apps.models import Category, Product
from apps.serializers import CategoryModelSerializer, ProductModelSerializer

@extend_schema(tags=["category"])

class CategoryListCreateAPIView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer

@extend_schema(tags=["category"])
class CategoryRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer
@extend_schema(tags=["product"])

class ProductListCreateAPIView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer

    # def post(self, request, *args, **kwargs):
    #     print(request)
