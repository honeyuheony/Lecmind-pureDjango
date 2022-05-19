from django.urls import path, include
from rest_framework.routers import DefaultRouter 
from .views import SubjectViewSet, LectureViewSet


# router = DefaultRouter()
# router.register('video-select', SubjectViewSet, basename="subject")
# router.register('lectuer', LectureViewSet, basename="lectuer")

urlpatterns = [
    # path('', include(router.urls)),
]