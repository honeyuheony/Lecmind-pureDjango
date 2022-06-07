import datetime
from operator import le
from re import A, sub
from unicodedata import name
from unittest import result
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from numpy import empty
# from patternProject.subject.views import learning

from subject.models import Lecture
from .models import User
from .forms import UserForm
# Create your views here.
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework_jwt.settings import api_settings

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
api_settings.JWT_EXPRIATION_DELTA = datetime.timedelta(days=7)

def home(request):  #cur_lectureID
    login_student = request.user
    
    if str(login_student)=='AnonymousUser':
        return redirect('signin')
    

    # lectures = Lecture.objects.filter(subject=tmp)
    # tmp =all_subject.values_list('name')
    # print(lectures)
    # all_lecture = Lecture.objects.filter(subject = subject_lecture.name)
    # all_lectures = Subject.prefetch_related('lecture_set')
    
    all_lectures= Lecture.objects.filter(student=login_student)
    all_subject = []
    
    if not all_lectures.exists():
        return render(request, 'init.html', {'login_student':login_student})
    else:
        for l in all_lectures:
            all_subject.append(l.subject)
        all_subject = set(all_subject)
        
        print(all_subject)
        lecture_info = Lecture.objects.all()
        context = {
            'lecture_info':lecture_info,
            'all_subject':all_subject,
            'login_student':login_student,
            'all_lectures': all_lectures
            # 'all_lecture': all_lecture
            # 'current_lecture':current_lecture
        }
    return render(request, 'home.html', context)
    # return render(request, 'home.html')


def signup(request):
    user_form = UserForm()
    if request.method == "POST":
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            return redirect('signin')
        return redirect('signup')
    return render(request, 'signup.html', {'regi_form':user_form})

@csrf_exempt
def signin(request):
    if str(request.user) != 'AnonymousUser':
        return redirect('home') # 일단 로그인 시 home으로 가도록 지정
    
    if request.method == "POST":
        id = request.POST.get('id','')
        password = request.POST.get('password','')
        user = authenticate(request, id=id, password=password)
        if user is not None:
            response = redirect('home')
            login(request, user)
            payload = jwt_payload_handler(user)
            token = jwt_encode_handler(payload)
            response.set_cookie(key = 'Authorization', value = f'{token}')
            request.session['id'] = id
            return response
    return render(request, 'signin.html')

def signout(request):
    return render(request, 'signin.html')


@login_required
def subject(request, sub):
    login_student = request.user
    all_lectures= Lecture.objects.filter(student=login_student).order_by('degree')
    
    all_subject = set()
    for l in all_lectures:
        all_subject.add(l.subject)
    
    subOFlecturs = Lecture.objects.filter(subject=sub)

    # all_subject = Subject.objects.filter(student=login_student)
    current_subject = Lecture.objects.filter(subject=sub).first()
    print(current_subject)
   
    # print(current_subject)
    # all_lecture = Lecture.objects.filter(subject=current_subject).order_by('degree')
    
    
    # lecture_info = Lecture.objects.all()
    
    context = {
        'login_student':login_student,
        'all_subject':all_subject,
        'all_lectures':all_lectures,
        'current_subject':current_subject,
        'subOFlecturs':subOFlecturs
    }
    return render(request, 'subjects.html', context)

def detail(request,id):
    login_student = request.user
    current_lecture = Lecture.objects.get(video_id=id)
    current_subject = current_lecture.subject
    
    # lecture_subject = Subject.objects.filter(student=request.user)
    
    lectureOFsubject = Lecture.objects.filter(subject=current_subject)
    all_lectures= Lecture.objects.filter(student=login_student)
    
    print(lectureOFsubject)
    
    all_subject = set()
    for l in all_lectures:
        all_subject.add(l.subject)
   
    # user = Lecture.objects.get()
    lecture_info = Lecture.objects.all()
    
    # print(login_student)
    # total_time = current_lecture.lecturetime
    # tt = total_time.split(':')
    # print(tt)
    
    context = {
        'lecture_info':lecture_info,
        'current_lecture':current_lecture,
        'login_student':login_student,
        'all_lectures':all_lectures,
        'current_subject':current_subject,
        'all_subject':all_subject,
        'lectureOFsubject':lectureOFsubject
    }
    
    # print(current_lecture)
    
    return render(request, 'detail.html', context)





@login_required
def signout(request):
    logout(request)
    request.COOKIES.Authorization = ''
    return redirect('signin')

# 수강과목 리스트
@login_required
def SubjectList(request):
    subject_list = Subject.objects.all()
    return render(request, 'home.html', {'subject':'name', 'subject_list':'subject_list'})

def LectureList(request, subject):
    lecture_list = Lecture.objects.get(id=subject)
    
        
