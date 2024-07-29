from django.conf import settings
from celery import shared_task

import requests


@shared_task
def send_telegram_message(*args):
    """Отправляет пользователю привчку в телеграм"""
    chat_id = args[0]
    message = args[1]

    params = {"chat_id": chat_id, "text": message}
    requests.get(
        f"{settings.TELEGRAM_URL}{settings.TELEGRAM_TOKEN}/sendMessage", params=params
    )
