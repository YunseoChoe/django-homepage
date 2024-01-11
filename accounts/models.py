from django.db import models
from django.contrib.auth.models import AbstractUser

# User 상속 모델에 필드 추가
class CustomUser(AbstractUser):
    age = models.IntegerField(null = True)
    height = models.IntegerField(null = True)
    weight = models.IntegerField(null = True)
