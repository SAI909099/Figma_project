from http import HTTPStatus

from django.core.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer

from apps.models import Category, Product


class ProductModelSerializer(ModelSerializer):
    class Meta:
        model = Product
        exclude = "slug" , "created_at"


class CategoryModelSerializer(ModelSerializer):
    class Meta:
        model = Category
        exclude = "slug",


    def validate(self, attrs):
        if len(attrs['name']) < 3:
            raise ValidationError('name uzunligi 3 tadan katta bo\'lsin', code=HTTPStatus.BAD_REQUEST)
        return attrs






