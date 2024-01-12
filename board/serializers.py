from rest_framework import serializers
from .models import Board

# create
class BoardSerializers(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = ['title', 'content', 'writer']
    
    def create(self, validated_data):
        board = Board(**validated_data)
        board.save()
        return board