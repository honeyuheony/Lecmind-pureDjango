from re import sub
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
# from patternProject.subject.views import learning

from subject.models import Lecture, Subject
from .models import User
from .forms import UserForm
# Create your views here.
from django.http import HttpResponse

def home(request):  #cur_lectureID
    # return HttpResponse("Hello, world. You're at the Home index.")
    login_student = request.user
    learning_time = Lecture.objects.all()
    
    lecture_subject = Subject.objects.filter(student=login_student)
    # all_lecture = Lecture.objects.filter(subject__in=lecture_subject, student__in=login_student)
    
    # current_lecture = request.GET[id]
    lecture_info = Lecture.objects.all()
    context = {
        'lecture_info':lecture_info,
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


def subject(request):
    lecture_info = Lecture.objects.all()
    
    context = {
        'lecture_info':lecture_info,
    }
    return render(request, 'subjects.html', context)

def detail(request,id):
    current_lecture = Lecture.objects.get(video_id=id)
    cl_subject = current_lecture.subject
    cl_student = cl_subject.student
    
    all_lecture = Lecture.objects.filter(subject=cl_subject)
    print(all_lecture)
    
    print(cl_student)
    print(cl_subject)
    print(current_lecture.name)
    # user = Lecture.objects.get()
    lecture_info = Lecture.objects.all()
    student = request.user
    # print(student)
    # total_time = current_lecture.lecturetime
    # tt = total_time.split(':')
    # print(tt)
    
    context = {
        'lecture_info':lecture_info,
        'current_lecture':current_lecture,
        'student':student,
        'all_lecture':all_lecture
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
    
        
