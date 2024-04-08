from rest_framework import serializers
from .models import Board, Comment

# create
class BoardSerializers(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = ['title', 'content', 'writer']
    
    def create(self, validated_data):
        board = Board(**validated_data)
        board.save()
        return board

class CommentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['auther', 'post', 'text'] # Comment 모델의 필드 지정
