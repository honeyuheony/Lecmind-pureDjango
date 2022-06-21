import sys
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
        self.set_analysis_data(image, analysis)
        _, jpeg = cv2.imencode('.jpg', image)   # 이미지파일 byte단위로 읽고 jpg로 디코딩
        return jpeg.tobytes()   # live video를 바이트단위 프레임으로 얻음

    def print_face(self, _frame):
        detector = dlib.get_frontal_face_detector()
        predictor = dlib.shape_predictor("./analysis/shape_predictor_68_face_landmarks.dat")
        gray = cv2.cvtColor(_frame, cv2.COLOR_BGR2GRAY)
        faces = detector(gray)
        RIGHT_EYE = list(range(36, 42))  
        LEFT_EYE = list(range(42, 48))  
        NOSE = list(range(27, 36))  
        for face in faces:
            facial_landmarks = predictor(gray, face)
            list_points = []
            for p in facial_landmarks.parts():
                list_points.append([p.x, p.y])
            list_points = np.array(list_points)
            for i,pt in enumerate(list_points[RIGHT_EYE]):
                pt_pos = (pt[0], pt[1])
                cv2.circle(_frame, pt_pos, 2, (0, 255, 0), -1)
            for i,pt in enumerate(list_points[LEFT_EYE]):
                pt_pos = (pt[0], pt[1])
                cv2.circle(_frame, pt_pos, 2, (0, 255, 0), -1)
            for i,pt in enumerate(list_points[NOSE]):
                pt_pos = (pt[0], pt[1])
                cv2.circle(_frame, pt_pos, 2, (0, 255, 0), -1)

    def get_test_frame(self):
        if self.grabbed:
            image = self.frame
            self.print_face(image)
            self.last_frame = image
        else:
            image = self.last_frame
        
        _, jpeg = cv2.imencode('.jpg', image)   # 이미지파일 byte단위로 읽고 jpg로 디코딩
        return jpeg.tobytes()   # live video를 바이트단위 프레임으로 얻음
    
    
        
    def update(self):   # 이미지로부터 비디오 생성
        while True:
            (self.grabbed, self.frame) = self.video.read()
            
            #self.video.release()


    
def gen(camera, analysis, test = False):    # (위의)특정한 프레임으로부터 인코딩된 비디오 얻음
    while True:
        if test:
            frame = camera.get_test_frame()
        else:
            frame = camera.get_frame(analysis)
        
        yield (b'--frame\r\n'
            b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
        
        
@gzip.gzip_page
def detectme(request, test = False):
    lecture = Lecture.objects.filter(student=request.user).latest('update_date')
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
        if test:
            return StreamingHttpResponse(gen(cam, analysis, True), content_type="multipart/x-mixed-replace;boundary=frame")
        else:
            return StreamingHttpResponse(gen(cam, analysis), content_type="multipart/x-mixed-replace;boundary=frame")
    except:
        pass

def analysis(request):
    return detectme(request, True)
    # Print face's area
# class AnalysisViewSet(viewsets.ModelViewSet):
#     queryset = Analysis.objects.all()
#     serializer_class = AnalysisSerializer

# class InteractionViewSet(viewsets.ModelViewSet):
#     queryset = Interaction.objects.all()
#     serializer_class = InteractionSerializer