from django.db import models

from django.contrib.auth.models import AbstractUser
from django.db import models
from rest_framework.fields import EmailField, CharField


class User(AbstractUser):
    email = EmailField()




class VerificationCode(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)

    def str(self):
        return f"{self.user.email} - {self.code}"


class Essential(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Unit(models.Model):
    title = models.CharField(max_length=255)
    essential = models.ForeignKey(Essential, on_delete=models.SET_NULL, null=True, blank=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title