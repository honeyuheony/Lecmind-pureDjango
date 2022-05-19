from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.chrome, name='chrome'),
    path('detectme/', views.detectme, name='detectme'),
]