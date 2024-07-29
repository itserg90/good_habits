from django.db import models

from config.settings import AUTH_USER_MODEL


class Habit(models.Model):
    user = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name="Пользователь",
    )
    place = models.CharField(
        max_length=100, blank=True, null=True, verbose_name="Место"
    )
    time = models.TimeField(verbose_name="Время")
    action = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="Действие"
    )
    pleasant_habit = models.BooleanField(
        default=False, null=True, blank=True, verbose_name="Признак приятной привычки"
    )
    related_habit = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="Связанная привычка",
    )
    periodicity = models.PositiveIntegerField(
        verbose_name="Периодичность в днях", default=1
    )
    reward = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name="Вознаграждение",
    )
    time_to_complete = models.DurationField(
        null=True, blank=True, verbose_name="Время на выполнение"
    )
    publicity = models.BooleanField(
        default=False, blank=True, null=True, verbose_name="Призгак публичности"
    )
    updated_at = models.DateTimeField(
        auto_now=True, blank=True, null=True, verbose_name="Дата изменения"
    )

    class Meta:
        verbose_name = "Привычка"
        verbose_name_plural = "Привычки"

    def __str__(self):
        return self.action
