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

from subject.models import Lecture, Subject
from .models import User
from .forms import UserForm
# Create your views here.
from django.http import HttpResponse

def home(request):  #cur_lectureID
    login_student = request.user
    
    if str(login_student)=='AnonymousUser':
        return redirect('signin')
    
    all_subject = Subject.objects.filter(student=login_student)
    # lectures = Lecture.objects.filter(subject=tmp)
    # tmp =all_subject.values_list('name')
    # print(lectures)
    # all_lecture = Lecture.objects.filter(subject = subject_lecture.name)
    # all_lectures = Subject.prefetch_related('lecture_set')
    if not all_subject.exists():
        return render(request, 'init.html', {'login_student':login_student})
    else:
        tmp = []
        for lecture in all_subject:
            tmp.append(Lecture.objects.filter(subject=lecture)) 
        
        all_lectures= tmp[0]
        print(all_lectures)
        for lec in tmp:
            all_lectures = all_lectures|lec
        
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


def signin(request):
    # if str(request.user) != 'AnonymousUser':
    #     return redirect('home') # 일단 로그인 시 home으로 가도록 지정
    
    if request.method == "POST":
        id = request.POST.get('id','')
        password = request.POST.get('password','')
        user = authenticate(request, id=id, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request, 'signin.html')

def signout(request):
    return render(request, 'signin.html')


def subject(request, sub):
    login_student = request.user
    all_subject = Subject.objects.filter(student=login_student)
    current_subject = Subject.objects.get(name=sub)
    all_lecture = Lecture.objects.filter(subject=current_subject).order_by('degree')
    
    
    lecture_info = Lecture.objects.all()
    
    context = {
        'login_student':login_student,
        'all_subject':all_subject,
        'all_lecture':all_lecture,
        'current_subject':current_subject
    }
    return render(request, 'subjects.html', context)

def detail(request,id):
    current_lecture = Lecture.objects.get(video_id=id)
    cl_subject = current_lecture.subject
    
    lecture_subject = Subject.objects.filter(student=request.user)
    
    all_lecture = Lecture.objects.filter(subject=cl_subject)
   
    # user = Lecture.objects.get()
    lecture_info = Lecture.objects.all()
    login_student = request.user
    # print(login_student)
    # total_time = current_lecture.lecturetime
    # tt = total_time.split(':')
    # print(tt)
    
    context = {
        'lecture_info':lecture_info,
        'current_lecture':current_lecture,
        'login_student':login_student,
        'all_lecture':all_lecture,
        'lecture_subject':lecture_subject
    }
    
    # print(current_lecture)
    
    return render(request, 'detail.html', context)





@login_required
def signout(request):
    logout(request)
    return redirect('signin')

# 수강과목 리스트
@login_required
def SubjectList(request):
    subject_list = Subject.objects.all()
    return render(request, 'home.html', {'subject':'name', 'subject_list':'subject_list'})

def LectureList(request, subject):
    lecture_list = Lecture.objects.get(id=subject)
    
        
