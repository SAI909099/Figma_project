from django.contrib.auth.views import LoginView
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.routers import DefaultRouter

from .views import UserCreateAPIView, SendEmail, BooksListCreateAPIView, UnitsListCreateAPIView, \
    UnitsDRetrieveUpdateDestroyAPIView

# router = DefaultRouter()
# # router.register(r'books', BooksListCreateAPIView)
# router.register(r'units', UnitsViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title="Unit API",
        default_version='v1',
        description="API documentation for Units",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@yourapi.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', UserCreateAPIView.as_view(), name='register'),
    # path('', include(router.urls)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('send_email', SendEmail.as_view()),
    path('books', BooksListCreateAPIView.as_view()),
    path('Units', UnitsListCreateAPIView.as_view()),
    path('Units/<int:pk>', UnitsDRetrieveUpdateDestroyAPIView.as_view()),

]
