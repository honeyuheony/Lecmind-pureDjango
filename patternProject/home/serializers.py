# serializer선언 (데이터표현 관련 정의)
from dataclasses import field
from .models import User
from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from django.contrib.auth import get_user_model, authenticate


User = get_user_model()

# Serializers define the API representation
class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user = User.objects.create_user(
            id = validated_data['id'],
            email = validated_data['email'],
            name = validated_data['name'],
            password = validated_data['password']
        )
        return user
    
    class Meta:
        model = User
        fields = ('name', 'id', 'password', 'email')


