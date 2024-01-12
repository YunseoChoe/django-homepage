from django.db import models

class Board(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField(max_length=100)
    writer = models.CharField(max_length=10)

