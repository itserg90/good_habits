from celery import shared_task
from habits.models import Habit
from habits.services import send_message, check_periodicity


@shared_task
def send_telegram_message():
    """Отправляет пользователю привчку в телеграм"""
    habits = Habit.objects.all()
    for habit in habits:
        if habit.user.tg_chat_id and check_periodicity(
            habit.updated_at, habit.periodicity
        ):
            tg_id = habit.user.tg_chat_id
            message = (
                f"Привычка: {habit.action}\nВремя: {habit.time}\nМесто: {habit.place}"
            )
            send_message(tg_id, message)
