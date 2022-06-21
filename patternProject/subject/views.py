from datetime import datetime
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views import generic
from .models import Lecture, Notes
from home.models import User
from .forms import *
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from .serializers import LectureSerializer, NotesSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsOwnerOrReadOnly

# 학습 동영상 선택
# 1. 과목방 생성 or 선택 ui를 통해 과목방 name post
# 2. 강의 url post
@csrf_exempt
def save_title(request):
    idx = request.POST.get('idx')
    lec = get_object_or_404(Lecture, pk = idx)
    lec.name = request.POST.get('memo')
    lec.save()
    note, create = Notes.objects.update_or_create(
        lecture = lec
    )
    note.content = request.POST.get('memo')
    note.save()
    return redirect(f"/learning/{lec.video_id}")

@csrf_exempt
def set_subject(request):
    idx = request.POST.get('idx')
    lec = get_object_or_404(Lecture, pk = idx)
    subject = request.POST.get('sub_name')
    lec.subject = subject
    lec.save()
    return redirect(f"/learning/{lec.video_id}")


@csrf_exempt
def create_subject(request):
    video_id = request.POST.get('video_id')
    subject = request.POST.get('sub_name')
    lec, create = Lecture.objects.update_or_create(
        student = subject,
        video_id = video_id
    )
    lec.subject = subject
    lec.save()
    return redirect(f"/learning/{video_id}")

@csrf_exempt
def finish_learning(request):
    idx = request.POST.get('idx')
    lec = get_object_or_404(Lecture, pk = idx)
    lec.state = 'completed'
    lec.degree = Lecture.objects.filter(student = lec.student, subject = lec.subject, state = 'completed').count()
    lec.complet_date = datetime.now()
    lecture_time = int(float(request.POST.get('lecture_time')))
    if lecture_time > 3600:
        lecture_time = str(lecture_time // 3600) + ':' + str((lecture_time % 3600) // 60) + ':' + str((lecture_time % 3600) % 60)
    elif lecture_time >= 60:
        lecture_time = str(lecture_time // 60) + ':' + str(lecture_time % 60)
    else:
        lecture_time = str(lecture_time)
    learning_time = int(float(request.POST.get('learning_time')))
    if learning_time > 3600:
        learning_time = str(learning_time // 3600) + ':' + str((learning_time % 3600) // 60) + ':' + str((learning_time % 3600) % 60)
    elif learning_time >= 60:
        learning_time = str(learning_time // 60) + ':' + str(learning_time % 60)
    else:
        learning_time = str(learning_time)

    lec.lecture_time = lecture_time
    lec.learning_time = learning_time
    lec.save()
    return redirect(f"/detail/{lec.video_id}")


@csrf_exempt
def learning(request, video_id):
    if request.method == "POST":
        # lecture 생성, 이미 있으면 기존 학습 데이터 불러오기
        lec, create = Lecture.objects.update_or_create(
            student = request.user,
            video_id = request.POST.get('url').split('=')[1]
        )
        if lec.lecture_time == None:
            lec.lecture_time = request.POST.get('video_length')
        lec.state = 'ongoing'
        lec.save()
    return render(request, 'learning.html', {'lecture':lec})


def learning_test(request, video_id):
    id = video_id
    lec = get_object_or_404(Lecture, video_id = id)
    subject = Lecture.objects.filter(student = lec.student).values('subject').order_by('subject').distinct()
    subject = subject.exclude(subject='과목 미지정')
    request.user = lec.student
    return render(request, 'learning.html', {'lecture':lec, 'subject': subject})

@login_required
def videotest(request):
    return render(request, 'videotest.html')
        


# # 입력받은 강의정보로 lecture 필드 생성
# # 입력받은 강의 url 통해 lecture 페이지 이동
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



# 강의수강 시작 전 강의분류 선택
            
