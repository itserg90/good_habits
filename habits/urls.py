from django.urls import path

from habits.apps import HabitsConfig
from habits.views import (
    HabitListAPIView,
    PublicHabitListAPIView,
    HabitCreateAPIView,
    HabitUpdateAPIView,
    HabitDeleteAPIView,
)

app_name = HabitsConfig.name
urlpatterns = [
    path("", HabitListAPIView.as_view(), name="habit_list"),
    path("public/", PublicHabitListAPIView.as_view(), name="public_habit_list"),
    path("habit/create/", HabitCreateAPIView.as_view(), name="habit_create"),
    path("habit/<int:pk>/update/", HabitUpdateAPIView.as_view(), name="habit_update"),
    path("habit/<int:pk>/delete/", HabitDeleteAPIView.as_view(), name="habit_delete"),
]
