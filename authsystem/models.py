from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
from .manager import UserManager

class CustomModel(AbstractUser):
    username = models.CharField(max_length = 10 , null = True)
    phone_number = models.CharField(max_length = 10, unique = True, null = True)
    email = models.EmailField(null = False, unique = True)
    bio = models.CharField(null = True, max_length = 100)
    


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


    objects = UserManager()

