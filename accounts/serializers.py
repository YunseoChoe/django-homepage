# 필요한 모듈 및 클래스를 임포트합니다.
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import serializers
from .models import CustomUser

# 회원가입을 위한 시리얼라이저를 정의합니다.
class UserSerializers(serializers.ModelSerializer):
    # Meta 클래스에서 모델과 필드를 설정합니다.
    class Meta:
        model = CustomUser
        fields = ['email', 'password', 'username', 'age', 'height', 'weight']
        # 비밀번호 필드는 쓰기 전용(write_only)으로 설정합니다.
        extra_kwargs = {'password': {'write_only': True}}

    # 사용자 생성 메서드를 오버라이드합니다.
    def create(self, validated_data):
        # 비밀번호를 추출합니다.
        password = validated_data.pop('password')
        # 사용자 객체를 생성합니다.
        user = CustomUser(**validated_data)
        # 비밀번호를 해싱하여 사용자 객체에 설정합니다.
        user.set_password(password)
        # 사용자를 저장합니다.
        user.save()

        # 회원가입 후에 사용자를 위한 리프레시 토큰과 액세스 토큰을 생성합니다.
        refresh = RefreshToken.for_user(user)
        # 생성된 토큰들을 JSON 형식으로 구성하여 반환합니다.
        tokens = {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }

        return tokens
