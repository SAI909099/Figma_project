from random import random

from django.core.mail import send_mail
from django.shortcuts import render
from django.views import View
from drf_spectacular.utils import extend_schema
from drf_yasg.utils import swagger_auto_schema
from rest_framework.generics import CreateAPIView

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets, generics, permissions
from django.contrib.auth import login
from rest_framework.authtoken.models import Token

from root import settings
from .models import Unit, Essential, User
from .serializers import LoginSerializer, UnitSerializer, EssentialSerializer, RegisterUserSerializer
# from .serializers import RegistrationSerializer
from .serializers import UserRegistrationSerializer

@extend_schema(tags=['user'])
class UserCreateAPIView(CreateAPIView):
    queryset = User.objects.all
    serializer_class = RegisterUserSerializer


class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data
            token, created = Token.objects.get_or_create(user=user)
            return Response({"token": token.key})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@extend_schema(tags=['user'])
class SendEmail(APIView):
    permission_classes = permissions.AllowAny,
    def post(self, request):
        receiver_email = request.POST['email']
        generate_code = random.randit(10**5 , 10**6)
        send_mail("Verification code",f"code : {generate_code}",settings.EMAIL_HOST_USER,[receiver_email] )
        return Response ({"message" : generate_code})


# class UserRegistrationView(APIView):
#     def post(self, request):
#         serializer = UserRegistrationSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"detail": "User registered successfully"}, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class UnitViewSet(viewsets.ModelViewSet):
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer


class EssentialViewSet(viewsets.ModelViewSet):
    queryset = Essential.objects.all()
    serializer_class = EssentialSerializer



class UnitListCreateView(generics.ListCreateAPIView):
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer

    @swagger_auto_schema(
        operation_description="Retrieve a list of units or create a new unit.",
        responses={200: UnitSerializer(many=True)},
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        request_body=UnitSerializer,
        responses={201: UnitSerializer},
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)




