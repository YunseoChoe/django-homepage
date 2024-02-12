from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate # login했을 때 데이터가 db에 있는 지 확인
from rest_framework import generics
from .serializers import UserSerializers
from rest_framework_simplejwt.tokens import RefreshToken
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
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        # 사용자 인증
        user = authenticate(username=username, password=password)
        
        if user is None:
            return Response({'error': 'Invalid username or password.'}, status=status.HTTP_400_BAD_REQUEST)
        
        # 토큰 발급
        refresh = RefreshToken.for_user(user) # Simple JWT의 RefreshToken.for_user() 메서드를 사용
        
        # 응답에 토큰 포함하여 반환
        return Response({
            'message': 'Login successful!',
            'refresh_token': str(refresh),                  # 리프레시 토큰
            'access_token': str(refresh.access_token),      # 액세스 토큰
        }, status=status.HTTP_200_OK)