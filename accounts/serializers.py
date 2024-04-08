from rest_framework import serializers
from .models import CustomUser

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['email', 'password', 'username', 'age', 'height', 'weight']
        # 비밀번호 필드는 쓰기 전용(write_only)으로 설정합니다.
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        # 비밀번호를 추출합니다.
        password = validated_data.pop('password')
        # 사용자 객체를 생성합니다.
        user = CustomUser(**validated_data)
        # 비밀번호를 해싱하여 사용자 객체에 설정합니다.
        user.set_password(password)
        # 사용자를 저장합니다.
        user.save()
        # 사용자 객체를 반환합니다.
        return user
