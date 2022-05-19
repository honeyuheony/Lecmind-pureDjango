from django.shortcuts import render
from .models import User
# Create your views here.
from django.http import HttpResponse
from .serializers import UserSerializer
from rest_framework import generics


def home(request):
    return HttpResponse("Hello, world. You're at the Home index.")
    # return render(request, 'chrom.html')

# 회원가입
class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer