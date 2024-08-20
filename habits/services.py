from datetime import datetime
from pytz import timezone

import requests

from config import settings


def check_periodicity(updated_at, periodicity):
    """Проверяет периодичность привычки"""
    current_time = datetime.now(timezone("UTC"))
    dt = (current_time - updated_at).days
    days_remaining = dt % periodicity
    if dt > 0 and days_remaining == 0:
        return True
    return False


def send_message(tg_id, message):
    params = {"chat_id": tg_id, "text": message}
    requests.get(
        f"{settings.TELEGRAM_URL}{settings.TELEGRAM_TOKEN}/sendMessage", params=params
    )
