from django.urls import path, include
from . import views
# from rest_framework.routers import DefaultRouter 
# from .views import SubjectViewSet, LectureViewSet


# router = DefaultRouter()
# router.register('video-select', SubjectViewSet, basename="subject")
# router.register('lectuer', LectureViewSet, basename="lectuer")


urlpatterns = [
    path('videotest', views.videotest, name='videotest'),
    path('', views.learning, name='learning'),
    path('<str:video_id>', views.learning_test, name='learning_test'),
    
]