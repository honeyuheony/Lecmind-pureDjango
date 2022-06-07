from django.urls import path, include

from . import views


urlpatterns = [
    path('', views.analysis, name='analysis'),
    path('detectme', views.detectme, name='detectme'),
    path('lecture_event', views.lecture_event, name='lecture_event')
]
