from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=225, null=True)
    last_name = models.CharField(max_length=225, null=True)
    username = models.CharField(max_length=225, unique=True)
    # password = models.CharField(max_length=225)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return f'{self.username} User'
