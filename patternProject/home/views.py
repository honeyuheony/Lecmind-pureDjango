from turtle import title
from django.shortcuts import redirect, render

from patternProject.subject.models import Lecture, Subject
from .models import User
# Create your views here.
from django.http import HttpResponse
from .serializers import UserSerializer
from rest_framework import generics


def home(request):
    return HttpResponse("Hello, world. You're at the Home index.")
    # return render(request, 'chrom.html')


def signup(request):
    user_form = UserCreationForm()
    if request.method == "POST":
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            return redirect('signin')
    return render(request, 'signup.html', {'regi_form':user_form})


def signin(request):
    if str(request.user) != 'AnonymousUser':
        return redirect('home') # 일단 로그인 시 home으로 가도록 지정
    
    if request.method == "POST":
        email = request.POST.get('email','')
        password = request.POST.get('password','')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request, 'signin.html')



@login_required
def signout(request):
    logout(request)
    return redirect('thank')



# 수강과목 리스트
@login_required
def SubjectList(request):
    subject_list = Subject.objects.all()
    return render(request, 'home.html', {'subject':'name', 'subject_list':'subject_list'})

def LectureList(request, subject):
    lecture_list = Lecture.objects.get(id=subject)
    
        
