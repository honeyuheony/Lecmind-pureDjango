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
from .tasks import Detect

import dlib
from math import hypot
import face_recognition
import numpy as np
import json

# Create your views here.
def analysis(request):
    return HttpResponse("Hello, world. You're at the analysis.")

# 학습 중 이벤트 기록
@csrf_exempt
def lecture_event(request):
    student = request.POST.get('student'),
    lec = get_object_or_404(Lecture, video_id = request.POST.get('lecture'), student=student)
    Interaction.objects.create(
        lecture = lec,
        interaction_type = request.POST.get('interaction_type'),
        interaction_time_real = request.POST.get('interaction_time_real'),
        interaction_time_lecture = request.POST.get('interaction_time_lecture')
    )
    return redirect(f"/learning/{request.POST.get('lecture')}")
    
# to capture video class
class VideoCamera(object):
    cnt = 0
    last_frame = ''
    def __init__(self):
        self.video = cv2.VideoCapture(0)    # 윈도우 디폴트 카메라 사용
        (self.grabbed, self.frame) = self.video.read()
        threading.Thread(target=self.update, args=()).start()
        
    def __del__(self):
        self.video.release()
        
    def set_analysis_data(self, image, analysis):
        cnt += 1
        if cnt == 10:
            cnt = 0
            param = image.tolist()
            frame_analysis_result = Detect.set_concentrate.delay(param)
            analysis.total_frames += 1
            if frame_analysis_result:
                analysis.focus_frames += 1
            analysis.concentration_rate = analysis.focus_frames / analysis.total_frames
            analysis.save()
            # 구간선정 구현하기

    def get_frame(self, analysis):
        if self.grabbed:
            image = self.frame
            self.last_frame = image
        else:
            image = self.last_frame
        # self.set_analysis_data(image, analysis)
        _, jpeg = cv2.imencode('.jpg', image)   # 이미지파일 byte단위로 읽고 jpg로 디코딩
        return jpeg.tobytes()   # live video를 바이트단위 프레임으로 얻음
    
    
        
    def update(self):   # 이미지로부터 비디오 생성
        while True:
            (self.grabbed, self.frame) = self.video.read()
            
            #self.video.release()


    
def gen(request, camera):    # (위의)특정한 프레임으로부터 인코딩된 비디오 얻음       
    while True:
        frame = camera.get_frame(request)
        
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
        
        
@gzip.gzip_page
def detectme(request):
    lecture = Lecture.objects.filter(student='admin').latest('update_date')
    analysis, create = Analysis.objects.update_or_create(
        lecture = lecture,
    )
    if analysis.total_frames:
        analysis.total_frames = 0
    if analysis.focus_frames:
        analysis.focus_frames = 0
    if analysis.concentration_rate:
        analysis.concentration_rate = 0
    analysis.save()
    
    try:
        cam = VideoCamera()
        # cam.get_frame()
        return StreamingHttpResponse(gen(analysis, cam), content_type="multipart/x-mixed-replace;boundary=frame")
    except:
        pass
# class AnalysisViewSet(viewsets.ModelViewSet):
#     queryset = Analysis.objects.all()
#     serializer_class = AnalysisSerializer

# class InteractionViewSet(viewsets.ModelViewSet):
#     queryset = Interaction.objects.all()
#     serializer_class = InteractionSerializer