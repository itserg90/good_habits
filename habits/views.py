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
from habits.services import check_periodicity
from habits.tasks import send_telegram_message


class HabitListAPIView(ListAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    pagination_class = CustomPaginator

    def get_queryset(self):
        queryset = super().get_queryset()
        habit_queryset = queryset.filter(user=self.request.user)
        for habit in habit_queryset:
            if habit.user.tg_chat_id:
                if check_periodicity(habit.updated_at, habit.periodicity):
                    idd = habit.user.tg_chat_id
                    # Собираем текст сообщения из полей habits
                    message = (
                        f"Привычка: {habit.action}\n"
                        f"Время: {habit.time}\n"
                        f"Место: {habit.place}"
                    )
                    send_telegram_message.delay(idd, message)
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
