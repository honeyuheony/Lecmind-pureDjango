# from unicodedata import name
from django.urls import path, include

from . import views

# app_name = 'home'
urlpatterns = [
    path('', views.home, name='home'),
    path('signup', views.signup, name='signup'),
    path('signin',views.signin, name='signin'),
    path('signout',views.signout, name='signout'),
    path('subject/<str:sub>',views.subject, name='subject'),
    path('detail/<str:id>', views.detail, name='detail'),
]
