from django.urls import path
from rest_framework.routers import DefaultRouter

from tracker.apps import TrackerConfig
from tracker.views import HabitViewSet, UserHabitAPIView

app_name = TrackerConfig.name
router = DefaultRouter()
router.register(r'habits', HabitViewSet, basename='habit')

urlpatterns = [
    path('my_habits/', UserHabitAPIView.as_view(), name='user_habit')
] + router.urls
