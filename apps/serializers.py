from django.contrib.auth import authenticate
from rest_framework import serializers

# from .models import VerificationCode
from django.contrib.auth.password_validation import validate_password
from rest_framework.serializers import ModelSerializer

from apps.models import User, Books, Units


class RegisterUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password',)

class BooksModelSerializer(ModelSerializer):
    class Meta:
        model = Books
        fields = '__all__'


class UnitsModelSerializer(ModelSerializer):
    class Meta:
        model = Units
        fields = '__all__'

    def to_representation(self, instance: Units):
        repr = super().to_representation(instance)
        repr['book'] = BooksModelSerializer(instance.book, context=self.context).data
        return repr

