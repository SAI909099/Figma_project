from django.contrib.auth import authenticate
from rest_framework import serializers
from django.contrib.auth.models import User
# from .models import VerificationCode
from django.contrib.auth.password_validation import validate_password

from apps.models import Essential, Unit


class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Invalid login credentials")

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password2')

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError("Passwords do not match.")
        return data

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class EssentialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Essential
        fields = ['id', 'name']


class UnitSerializer(serializers.ModelSerializer):
    essential = EssentialSerializer(read_only=True)
    essential_id = serializers.PrimaryKeyRelatedField(queryset=Essential.objects.all(), source='essential', write_only=True)

    class Meta:
        model = Unit
        fields = ['id', 'title', 'essential', 'essential_id', 'is_published']






