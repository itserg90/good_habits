from rest_framework.exceptions import ValidationError


class HabitRewardValidator:
    """Исключает одновременный выбор связанной привычки и указания вознаграждения"""

    def __init__(self, field):
        self.field = field

    def __call__(self, values):
        related_habit = values.get("related_habit")
        reward = values.get("reward")
        if related_habit and reward:
            raise ValidationError("Нужно указать либо привычку, либо вознаграждение")


class TimeToCompleteValidator:
    """Проверяет, чтобы, время выполнения было не более 120 секунд"""

    def __init__(self, field):
        self.field = field

    def __call__(self, time_to_complete):
        time_to_complete = time_to_complete.get("time_to_complete")
        if time_to_complete and time_to_complete.seconds > 121:
            raise ValidationError("Время выполнения должно быть не больше 120 секунд")


class PleasantHabitValidator:
    """Проверяет, что в связанные привычки могут попадать только привычки с признаком приятной привычки"""

    def __init__(self, field):
        self.field = field

    def __call__(self, related_habit):
        related_habit = related_habit.get("related_habit")
        if related_habit and not related_habit.pleasant_habit:
            raise ValidationError(
                "В связанные привычки должны указываться только привычки с признаком приятной привычки"
            )


class RelatedHabitRewardValidator:
    """Проверяет на отсутствие у приятной привычки вознаграждения или связанной привычки."""

    def __init__(self, field):
        self.field = field

    def __call__(self, values):
        pleasant_habit = values.get("pleasant_habit")
        related_habit = values.get("related_habit")
        reward = values.get("reward")
        if pleasant_habit and (related_habit or reward):
            raise ValidationError(
                "У приятной привычки не может быть вознаграждения или связанной привычки."
            )
