from django.shortcuts import render
from rest_framework import generics
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from home.models import Lecture,keyboard
from .serializers import LectureInfoSerializer ,KeyboardInterruptSerializer


# 제네릭 이용
# class PostChooseLecture(generics.CreateAPIView):
#     queryset = Lecture.objects.subject
#     serializer_class = LectureInfoSerializer


# class PostPlayLectureInfo(generics.CreateAPIView):
#     queryset = Lecture.objects.all()
#     serializer_class = LectureInfoSerializer
    

# viewset 이용
# Lecture
class LectureInfoViewSet(ModelViewSet):
    queryset = Lecture.objects.all()
    serializer_class = LectureInfoSerializer
    
    # 추가 매핑필요시 맴버함수로 구현
    # 참고 : https://ssungkang.tistory.com/entry/Django-ViewSet-%EA%B3%BC-Router?category=366160

lecture_list = LectureInfoViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
    
lecture_detail = LectureInfoViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})


# keyboard
class KeyboardInterruptViewSet(ModelViewSet):
    queryset = keyboard.objects.all()
    serializer_class = KeyboardInterruptSerializer


keyboard_list = KeyboardInterruptViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

keyboard_detail = KeyboardInterruptViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})