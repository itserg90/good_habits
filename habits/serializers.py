from rest_framework.serializers import ModelSerializer

from habits.models import Habit
from habits.validators import (
    HabitRewardValidator,
    TimeToCompleteValidator,
    PleasantHabitValidator,
    RelatedHabitRewardValidator,
)


class HabitSerializer(ModelSerializer):
    class Meta:
        model = Habit
        fields = "__all__"
        validators = [
            HabitRewardValidator(fields),
            TimeToCompleteValidator(field="time_to_complete"),
            PleasantHabitValidator(field="pleasant_habit"),
            RelatedHabitRewardValidator(fields),
        ]
