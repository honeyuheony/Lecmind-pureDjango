from django.urls import path,include
from rest_framework.routers import DefaultRouter 
from . import views

router = DefaultRouter()
router.register(r'lecture',views.LectureInfoViewSet,basename="lecture")
router.register(r'keyboard',views.KeyboardInterruptViewSet, basename="keyboard")


# urlpatterns = [
#     path('lecture/', views.lecture_list),
#     path('lecture/<int:pk>/', views.lecture_detail),
# ]

urlpatterns = [
    path('',include(router.urls)),
]
