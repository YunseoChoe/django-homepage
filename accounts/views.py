from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate # login했을 때 데이터가 db에 있는 지 확인
from rest_framework import generics
from .serializers import UserSerializers

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.http import HttpResponse

User = get_user_model()

# 회원가입
class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = UserSerializers

# 로그인
class LoginAPIView(APIView):
    # POST 메서드를 정의합니다.
    def post(self, request):
        # POST 요청에서 'username'과 'password' 데이터를 가져옵니다.
        username = request.data.get('username')
        password = request.data.get('password')

        # authenticate 함수를 사용하여 사용자를 인증합니다. (해당 사용자가 존재하고 비밀번호가 올바른지 확인)
        user = authenticate(username=username, password=password)
        
        # 사용자가 존재하지 않으면 에러 응답을 반환합니다.
        if user is None:
            return Response({'error': 'Invalid username or password.'}, status=status.HTTP_400_BAD_REQUEST)
        
        # 사용자가 존재하면 "success login!" 메시지를 포함한 응답을 반환합니다.
        response = HttpResponse("success login!")
        return response