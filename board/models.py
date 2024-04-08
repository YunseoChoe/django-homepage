from django.db import models
from accounts.models import CustomUser
from django.utils import timezone

# 게시판 Model
class Board(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField(max_length=100)
    writer = models.CharField(max_length=10)

# 댓글 Model
class Comment(models.Model):
    author = models.ForeignKey(CustomUser, on_delete = models.CASCADE)
    post = models.ForeignKey(Board, related_name = 'comments', on_delete = models.CASCADE)
    text = models.TextField()


