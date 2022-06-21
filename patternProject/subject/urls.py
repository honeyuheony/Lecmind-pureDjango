from django.urls import path, include
from . import views
# from rest_framework.routers import DefaultRouter 
# from .views import SubjectViewSet, LectureViewSet


# router = DefaultRouter()
# router.register('video-select', SubjectViewSet, basename="subject")
# router.register('lectuer', LectureViewSet, basename="lectuer")

app_name = 'subject'
urlpatterns = [
    path('videotest', views.videotest, name='videotest'),
    path('', views.learning, name='learning'),
    path('set_subject', views.set_subject, name='set_subject'),
    path('save_title', views.save_title, name='save_title'),
    path('finish_learning', views.finish_learning, name='finish_learning'),
    path('create_subject', views.create_subject, name='create_subject'),
    path('<str:video_id>', views.learning_test, name='learning_test'),


]