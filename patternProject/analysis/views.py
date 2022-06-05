from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from rest_framework.decorators import api_view
from django.http import HttpResponse
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Analysis, Interaction, Lecture
from .serializers import AnalysisSerializer, InteractionSerializer
import cv2, threading, os
from django.views.decorators import gzip
from django.http import HttpResponse, StreamingHttpResponse
from .tasks import *

import dlib
from math import hypot
import face_recognition
import numpy as np

# Create your views here.
def analysis(request):
    return HttpResponse("Hello, world. You're at the analysis.")

# 학습 중 이벤트 기록
@csrf_exempt
def lecture_event(request):
    lec = get_object_or_404(Lecture, pk=request.POST.get('lecture'))
    Interaction.objects.create(
        lecture = lec,
        interaction_type = request.POST.get('interaction_type'),
        interaction_time_real = request.POST.get('interaction_time_real'),
        interaction_time_lecture = request.POST.get('interaction_time_lecture')
    )
    return redirect(f"/learning/{request.POST.get('lecture')}")
    
# to capture video class
class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)    # 윈도우 디폴트 카메라 사용
        (self.grabbed, self.frame) = self.video.read()
        threading.Thread(target=self.update, args=()).start()
        
    def __del__(self):
        self.video.release()
        
    def get_frame(self):
        image = self.frame
        set_concentrate.delay(image)
        _, jpeg = cv2.imencode('.jpg', image)   # 이미지파일 byte단위로 읽고 jpg로 디코딩
        return jpeg.tobytes()   # live video를 바이트단위 프레임으로 얻음
        
    def update(self):   # 이미지로부터 비디오 생성
        while True:
            (self.grabbed, self.frame) = self.video.read()
            #self.video.release()


    
def gen(camera):    # (위의)특정한 프레임으로부터 인코딩된 비디오 얻음       
    while True:
        frame = camera.get_frame()
        
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
        
        
@gzip.gzip_page
def detectme(request):
    try:
        cam = VideoCamera()
        return StreamingHttpResponse(gen(cam), content_type="multipart/x-mixed-replace;boundary=frame")
    except:
        pass
# class AnalysisViewSet(viewsets.ModelViewSet):
#     queryset = Analysis.objects.all()
#     serializer_class = AnalysisSerializer

# class InteractionViewSet(viewsets.ModelViewSet):
#     queryset = Interaction.objects.all()
#     serializer_class = InteractionSerializer