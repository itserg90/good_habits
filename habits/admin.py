from django.contrib import admin

from habits.models import Habit


@admin.register(Habit)
class CourseAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "id",
        "place",
        "time",
        "action",
        "pleasant_habit",
        "related_habit",
        "periodicity",
        "reward",
        "time_to_complete",
        "publicity",
        "updated_at",
    )
