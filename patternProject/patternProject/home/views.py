from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout

from subject.models import Lecture, Subject
from .models import User
from .forms import UserForm
# Create your views here.
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

def home(request):
    # return HttpResponse("Hello, world. You're at the Home index.")
    return render(request, 'home.html')

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
    # if str(request.user) != 'AnonymousUser':
    #     return redirect('home') # 일단 로그인 시 home으로 가도록 지정
    
    if request.method == "POST":
        id = request.POST.get('id','')
        password = request.POST.get('password','')
        user = authenticate(request, id=id, password=password)
        if user is not None:
            login(request, user)
            request.session['id'] = id
            return redirect('home')
    return render(request, 'signin.html')


def detail(request):
    return render(request, 'detail.html')





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
    
        
