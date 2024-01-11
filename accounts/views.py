from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from rest_framework import generics
from .serializers import UserSerializers

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.http import HttpResponse

User = get_user_model()

class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = UserSerializers


class LoginAPIView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username = username, password=password)
        if user is None:
            return Response({'error': 'Invalid username or password.'}, status=status.HTTP_400_BAD_REQUEST)
        
        response = HttpResponse("success login!")
        return response
