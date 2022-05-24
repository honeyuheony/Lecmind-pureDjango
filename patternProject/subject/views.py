from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.urls import reverse
from django.views import generic
from .models import Subject, Lecture, Notes
from home.models import User
from .forms import *

# 학습 동영상 선택
# 1. 과목방 생성 or 선택 ui를 통해 과목방 name post
# 2. 강의 url post
@login_required
def learning(request):
    if request.method == "POST":
        sb, create = Subject.objects.update_or_create(
            student = request.user,
            name = request.POST.get('subject_name')
        )
        sb.save()
        # lecture 생성, 이미 있으면 기존 학습 데이터 불러오기
        lec, create = Lecture.objects.update_or_create(
            subject = sb,
            video_id = request.POST.get('url').split('=')[1]
        )
        if lec.degree == None:
            lec.degree = Lecture.objects.filter(subject = sb).count() + 1
        if lec.name == None:
            lec.name = str(sb.name) + '_' + str(lec.degree)
        if lec.lecture_time == None:
            lec.lecture_time = request.POST.get('video_length')
        lec.state = 'ongoing'
        lec.save()
    return render(request, 'learning.html', {'lecture':lec})

@login_required
def learning_test(request, video_id = None):
    if request.method == "POST":
        sb, create = Subject.objects.update_or_create(
            student = request.user.id,
            name = request.POST.get('name')
        )
        sb.save()
        # lecture 생성, 이미 있으면 기존 학습 데이터 불러오기
        lec, create = Lecture.objects.update_or_create(
            student = request.user.id,
            subject = sb,
            url = request.Post.get('video_id')
        )
        if lec.degree == None:
            lec.degree = Lecture.objects.count(subject = sb) + 1
        if lec.name == None:
            lec.name = str(sb.name) + '_' + str(lec.degree)
        if lec.lecture_time == None:
            lec.lecture_time = request.Post.get('video_length')
        lec.state = 'ongoing'
        lec.save()
    else:
        lec = get_object_or_404(Lecture, pk = video_id)
    return render(request, 'learning.html', {'lecture':lec})

@login_required
def videotest(request):
    return render(request, 'videotest.html')
        
# # 강의 영상 선택 & 강의 페이지 이동
# @api_view(['POST'])
# def video_select():
#     # 입력받은 강의정보로 lecture 필드 생성
#     # 입력받은 강의 url 통해 lecture 페이지 이동
#     pass

# # 학습시작 기록
# @api_view(['POST'])
# def start():
#     pass

# # 학습종료 기록
# @api_view(['POST'])
# def finish():
#     pass

# #결과 페이지 이동

# # 메모 중간저장
# @api_view(['POST'])
# def note_autosave():
#     pass

# # 마이페이지 강의 선택 (user view에 구현)
# # 복습환경 이동


# # 과목 정보 입력받기
# class SubjectViewSet(ModelViewSet):
#     queryset = Subject.objects.all()
#     serializer_class = SubjectSerializer
#     permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
#     def perform_create(self, serializer):
#         serializer.save(student = self.request.user)



# # 입력받은 강의정보로 lecture 필드 생성
# # 입력받은 강의 url 통해 lecture 페이지 이동

# class LectureViewSet(ModelViewSet):
#     queryset = Lecture.objects.all()
#     serializer_class = LectureSerializer
#     permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
#     # lectuer페이지 이동
#     # def perform_create(self, serializer):
#     #     sub_name = serializer.
#     #     sub = Subject.objects.get(name="객체지향개발론")
#     #     serializer.save(subject = sub)



# class NotesViewSet(ModelViewSet):
#     queryset = Notes.objects.all()
#     serializer_class = NotesSerializer
    

    
# class VideoSelectView(generic.ListView):
#     template_name: str



# 강의수강 시작 전 강의분류 선택
            


    
