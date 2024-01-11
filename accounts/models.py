from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    age = models.IntegerField(null = True)
    height = models.IntegerField(null = True)
    weight = models.IntegerField(null = True)
