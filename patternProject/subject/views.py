from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.urls import reverse
from django.views import generic
from .models import Subject, Lecture, Notes
from home.models import User
from .forms import *


# 강의 영상 선택 & 강의 페이지 이동
@api_view(['POST'])
def video_select():
    # 입력받은 강의정보로 lecture 필드 생성
    # 입력받은 강의 url 통해 lecture 페이지 이동
    pass

# 학습시작 기록
@api_view(['POST'])
def start():
    pass

# 학습종료 기록
@api_view(['POST'])
def finish():
    pass

#결과 페이지 이동

# 메모 중간저장
@api_view(['POST'])
def note_autosave():
    pass

# 마이페이지 강의 선택 (user view에 구현)
# 복습환경 이동


# 과목 정보 입력받기
class SubjectViewSet(ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    def perform_create(self, serializer):
        serializer.save(student = self.request.user)



# 입력받은 강의정보로 lecture 필드 생성
# 입력받은 강의 url 통해 lecture 페이지 이동

class LectureViewSet(ModelViewSet):
    queryset = Lecture.objects.all()
    serializer_class = LectureSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    # lectuer페이지 이동
    # def perform_create(self, serializer):
    #     sub_name = serializer.
    #     sub = Subject.objects.get(name="객체지향개발론")
    #     serializer.save(subject = sub)



# class NotesViewSet(ModelViewSet):
#     queryset = Notes.objects.all()
#     serializer_class = NotesSerializer
    

    
# class VideoSelectView(generic.ListView):
#     template_name: str

# 마이페이지에서 수강강좌 등록
@login_required
def AddSubject(request):
    username= request.GET.get('name','')
    subject_form = AddSubjectForm()
    if request.method == "POST":
        subject_form = AddSubjectForm(request.POST)
        if subject_form.is_valid():
            subject = subject_form.save(commit=False)
            subject.save()
            return redirect('home/')
    
    return render(request, 'home/home.html', {'subject_form':subject_form})

# 강의수강 시작 전 강의분류 선택
            


    
