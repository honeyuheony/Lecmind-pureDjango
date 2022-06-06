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

# class AnalysisViewSet(viewsets.ModelViewSet):
#     queryset = Analysis.objects.all()
#     serializer_class = AnalysisSerializer

# class InteractionViewSet(viewsets.ModelViewSet):
#     queryset = Interaction.objects.all()
#     serializer_class = InteractionSerializer