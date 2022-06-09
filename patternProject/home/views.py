import datetime
from unicodedata import name
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from numpy import empty
# from patternProject.subject.views import learning

from subject.models import Lecture
from .models import User
from analysis.models import Review_section, Analysis, Interaction
from .forms import UserForm
# Create your views here.
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework_jwt.settings import api_settings

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
api_settings.JWT_EXPRIATION_DELTA = datetime.timedelta(days=7)

def str2minT(st):
        st = list(map(int,st))
        
        res=0
        if(len(st)==3):
            res+= (st[0]*60 + st[1] + st[0]/60)
        elif(len(st)==2):
            res+= (st[0] + st[1]/60)
        else:
            res+=(st[0]/60)
        return res

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
    all_concen = []
    all_lnT=0
    
    
    if not all_lectures.exists():
        return render(request, 'init.html', {'login_student':login_student})
    else:
        for l in all_lectures:
            all_subject.append(l.subject)
            all_lnT += str2minT(l.learning_time.split(":"))     # 총 수강시간
            all_concen += Analysis.objects.filter(lecture=l.idx)
    
        
        all_con=0
        for i in all_concen:
            all_con += i.concentration_rate
        
        all_con /= len(all_concen)
        all_con = round(all_con, 2)
        all_lnT = round((all_lnT/60),2)
        
        # all_lnT.split(".")
        # print(all_lnT)
        # all_lnT = list(map(int,all_lnT))
        # if all_lnT[1] > 60:
        #     all_lnT[0] +=1
        #     all_lnT[1] -=60
         
       
        
        
        
        
        all_subject = set(all_subject)
        lecture_info = Lecture.objects.all()
        
        
        context = {
            'lecture_info':lecture_info,
            'all_subject':all_subject,
            'login_student':login_student,
            'all_lectures': all_lectures,
            'all_con': all_con,
            'all_lnT':all_lnT
            
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
            print(api_settings.JWT_EXPRIATION_DELTA)
            response.set_cookie(key = 'Authorization', value = f'{token}')
            request.session['id'] = id
            return response
    return render(request, 'signin.html')

def signout(request):
    logout(request)
    request.COOKIES['Authorization'] = ''
    return redirect('signin')


@login_required
def subject(request, sub):
    login_student = request.user
    all_lectures= Lecture.objects.filter(student=login_student).order_by('degree')
    
    all_subject = set()
    for l in all_lectures:
        all_subject.add(l.subject)
        
    
    all_concen = []
    subOFlecturs = Lecture.objects.filter(subject=sub)
    for l in subOFlecturs:
        all_concen += Analysis.objects.filter(lecture=l.idx)
    
    all_con=0
    for i in all_concen:
        all_con += i.concentration_rate

    all_con /= len(all_concen)
    all_con = round(all_con, 2)

    # all_subject = Subject.objects.filter(student=login_student)
    current_subject = Lecture.objects.filter(subject=sub).first()
    
   
    # print(current_subject)
    # all_lecture = Lecture.objects.filter(subject=current_subject).order_by('degree')
    
    
    # lecture_info = Lecture.objects.all()
    
    context = {
        'login_student':login_student,
        'all_subject':all_subject,
        'all_lectures':all_lectures,
        'current_subject':current_subject,
        'subOFlecturs':subOFlecturs,
        'all_con': all_con
    }
    return render(request, 'subjects.html', context)


@login_required
def detail(request,id):
    login_student = request.user
    current_lecture = Lecture.objects.get(video_id=id)
    current_subject = current_lecture.subject
    
    
    all_lectures= Lecture.objects.filter(student=login_student)
    lectureOFsubject = Lecture.objects.filter(subject=current_subject)      # 해당과목의 강의들
    # current_analysis = Analysis.objects.filter(lecture=current_lecture.idx)
    
    all_subject = set()
    for l in all_lectures:
        all_subject.add(l.subject)
    
    # 해당강의에 대한 분석 데이터
    review_section = Review_section.objects.filter(lecture=current_lecture)
    
    # 해당과목의 전체강의들에 대한 리뷰구간데이터
    all_rs=[]
    all_lnt=[]
    for lec in lectureOFsubject:    # 
        rs = Review_section.objects.filter(lecture=lec)
        all_lnt.append(round(str2minT(lec.learning_time.split(":")),2)) # 강의 lec의 수강시간
        tmp=0
        for i in rs:
            sec = str2minT((i.section_end).split(":")) - str2minT((i.section_start).split(":"))
            tmp+=round(sec,2)
        all_rs.append(tmp)  # 강의lec의 모든 reviewsection 구간길이
    
    percent = [int(round(all_rs[i]/all_lnt[i],2)*100) for i in range(len(all_rs))]
            
        
    
    # print(all_review_section)
    # print(review_section)
    
    
    
    
    
    # 집중도 데이터
    analysis_data = Analysis.objects.get(lecture=current_lecture)
    
    # 인터렉션 데이터
    # interaction_data = Interaction.objects.get(lecture=current_lecture.idx)
    
    
    # js용 정보
    cl_lec_lnt = current_lecture.lecture_time
    
    context = {
        'current_lecture':current_lecture,
        'login_student':login_student,
        'all_lectures':all_lectures,
        'current_subject':current_subject,
        'all_subject':all_subject,
        'lectureOFsubject':lectureOFsubject,
        'review_section':review_section,
        'cl_lec_lnt': cl_lec_lnt,
        'analysis_data': analysis_data,
        
        'all_rs':all_rs,
        'all_lnt':all_lnt,
        'percent':percent
    }
    
    # print(current_lecture)
    
    return render(request, 'detail.html', context)







# 수강과목 리스트
@login_required
def SubjectList(request):
    subject_list = Subject.objects.all()
    return render(request, 'home.html', {'subject':'name', 'subject_list':'subject_list'})

def LectureList(request, subject):
    lecture_list = Lecture.objects.get(id=subject)
    
        
