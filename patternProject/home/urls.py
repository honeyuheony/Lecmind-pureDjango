# from unicodedata import name
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.UserCreate.as_view()),
    # path('signin/', views.UserCreate.as_view()),
    path('api-auth/', include('rest_framework.urls')),
]
