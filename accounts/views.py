from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate # login했을 때 데이터가 db에 있는 지 확인
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import generics
from .serializers import UserSerializers
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.http import HttpResponse
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated

User = get_user_model()

# 회원가입
class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = UserSerializers

# 로그인
class LoginAPIView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        # print(username)
        # print(password)
        # 사용자 인증
        user = authenticate(username=username, password=password)
        
        if user is None:
            return Response({'error': 'Invalid username or password.'}, status=status.HTTP_400_BAD_REQUEST)
        
        # 토큰 발급
        refresh = RefreshToken.for_user(user) # Simple JWT의 RefreshToken.for_user() 메서드를 사용
        
        # 응답에 토큰 포함하여 반환
        response_data = {
            'message': 'success',
            'access_token': str(refresh.access_token),
            'refresh_token': str(refresh)
        }

        return JsonResponse(response_data, status=status.HTTP_200_OK)

# 사용자 정보
# class UserInfoAPIView(APIView):
#     def get(self, request):
#         # 클라이언트에서 AccessToken을 쿠키로부터 가져옴
#         access_token = request.COOKIES.get('access_token')
#         if not access_token:
#             return JsonResponse({'error': 'AccessToken이 존재하지 않습니다.'}, status=400)
#         try:
#             # JWTAuthentication 인스턴스를 생성하여 사용자 인증
#             jwt_authentication = JWTAuthentication()
#             # 요청을 사용하여 사용자를 인증합니다.
#             user, _ = jwt_authentication.authenticate(request)
            
#             # 인증된 사용자가 없으면 오류 반환
#             if not user:
#                 return JsonResponse({'error': '유저를 찾을 수 없습니다.'}, status=400)
#             # 인증된 사용자가 있을 경우, 유저 정보를 json으로 반환
#             return JsonResponse({'user': user.username})
        
#         # 예외 처리
#         except Exception as e:
#             # 예외가 발생하면 AccessToken을 파싱하는 중에 오류가 발생했음을 나타내는 JSON 응답을 반환합니다.
#             return JsonResponse({'error': 'AccessToken을 파싱하는 중 오류가 발생했습니다.'}, status=400)
    
class UserInfoAPIView(APIView):
    permission_classes = [IsAuthenticated]  # 인증된 사용자만 접근 가능하도록 설정

    def get(self, request):
        # 현재 요청을 보낸 사용자를 가져옴
        user = request.user
        # 사용자의 username을 포함한 응답을 반환
        return Response({'username': user.username})
