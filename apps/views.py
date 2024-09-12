import random

from django.core.mail import send_mail
from drf_spectacular.utils import extend_schema
from rest_framework import permissions
from rest_framework.generics import CreateAPIView, ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from root import settings
from .filters import UnitFilterSet
from .models import User, Books, Units
from .serializers import RegisterUserSerializer, \
    BooksModelSerializer, UnitsModelSerializer


@extend_schema(tags=['user'])
class UserCreateAPIView(CreateAPIView):
    queryset = User.objects.all
    serializer_class = RegisterUserSerializer


@extend_schema(tags=['user'])
class SendEmail(APIView):
    permission_classes = permissions.AllowAny,
    def post(self, request):
        receiver_email = request.POST['email']
        generate_code = random.randint(10 ** 5, 10 ** 6)
        send_mail("Verification code",f"code : {generate_code}",settings.EMAIL_HOST_USER,[receiver_email] )
        return Response ({"message" : "generate_code"})



@extend_schema(tags=['book'])
class BooksListCreateAPIView(ListCreateAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksModelSerializer


@extend_schema(tags=['units'])
class UnitsListCreateAPIView(ListCreateAPIView):
    queryset = Units.objects.all()
    serializer_class = UnitsModelSerializer
    filterset_class = UnitFilterSet


@extend_schema(tags=['Units'])
class UnitsDRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Units.objects.all()
    serializer_class = UnitsModelSerializer



