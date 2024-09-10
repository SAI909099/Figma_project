from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, viewsets, generics
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Unit, Essential
from .serializers import LoginSerializer, UnitSerializer, EssentialSerializer, RegistrationSerializer
from .serializers import UserRegistrationSerializer


class RegisterView(APIView):
    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, created = Token.objects.get_or_create(user=user)
            return Response({"token": token.key}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data
            token, created = Token.objects.get_or_create(user=user)
            return Response({"token": token.key})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class UserRegistrationView(APIView):
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"detail": "User registered successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



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




