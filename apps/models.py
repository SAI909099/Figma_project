from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass





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


