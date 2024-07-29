from datetime import datetime
from pytz import timezone


def check_periodicity(updated_at, periodicity):
    """Проверяет периодичность привычки"""
    current_time = datetime.now(timezone("UTC"))
    dt = (current_time - updated_at).days
    days_remaining = dt % periodicity
    if dt > 0 and days_remaining == 0:
        return True
    return False
