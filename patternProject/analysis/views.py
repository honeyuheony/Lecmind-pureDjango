from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from rest_framework.decorators import api_view
from django.http import HttpResponse
from django.urls import path
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Analysis, Interaction
from .serializers import AnalysisSerializer, InteractionSerializer

# Create your views here.
def analysis(request):
    return HttpResponse("Hello, world. You're at the analysis.")
# 학습 일시정지 기록
@api_view(['POST'])
def pause():
    pass

# 학습 일시정지 해제 기록
@api_view(['POST'])
def redo():
    pass

# 학습 영상 넘기기 기록
@api_view(['POST'])
def fast_forward():
    pass

# 학습 영상 뒤로가기 기록
@api_view(['POST'])
def rewind():
    pass

class AnalysisViewSet(viewsets.ModelViewSet):
    queryset = Analysis.objects.all()
    serializer_class = AnalysisSerializer

class InteractionViewSet(viewsets.ModelViewSet):
    queryset = Interaction.objects.all()
    serializer_class = InteractionSerializer