from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    UpdateAPIView,
    DestroyAPIView,
)

from habits.models import Habit
from habits.paginators import CustomPaginator
from habits.permissions import IsOwner
from habits.serializers import HabitSerializer


class HabitListAPIView(ListAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    pagination_class = CustomPaginator

    def get_queryset(self):
        queryset = super().get_queryset()
        habit_queryset = queryset.filter(user=self.request.user)

        return habit_queryset


class PublicHabitListAPIView(ListAPIView):
    queryset = Habit.objects.filter(publicity=True)
    serializer_class = HabitSerializer
    pagination_class = CustomPaginator


class HabitCreateAPIView(CreateAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer

    def perform_create(self, serializer):
        habit = serializer.save()
        habit.user = self.request.user
        habit.save()


class HabitUpdateAPIView(UpdateAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = (IsOwner,)


class HabitDeleteAPIView(DestroyAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = (IsOwner,)
