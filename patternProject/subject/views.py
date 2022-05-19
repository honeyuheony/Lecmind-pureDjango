from django.shortcuts import get_object_or_404, render
from rest_framework.decorators import api_view
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
# from rest_framework.decorators import detail_route, list_route
from .models import Subject, Lecture, Notes
from .serializers import SubjectSerializer, LectureSerializer, NotesSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsOwnerOrReadOnly
# Create your views here.


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



class NotesViewSet(ModelViewSet):
    queryset = Notes.objects.all()
    serializer_class = NotesSerializer