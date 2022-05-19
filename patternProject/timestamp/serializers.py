from dataclasses import field
from home.models import User , Lecture, keyboard    # 내가 만든 모델 import하기
from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from django.contrib.auth import get_user_model, authenticate


class LectureInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lecture
        field = '__all__'
        

class KeyboardInterruptSerializer(serializers.ModelSerializer):
    class Meta:
        model = keyboard
        field = '__all__'