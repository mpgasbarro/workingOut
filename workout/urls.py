from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('workout/', views.WorkoutList.as_view(), name='workout_list'),
    path('workout/<int:pk>', views.WorkoutDetail.as_view(), name='workout_detail'),
]