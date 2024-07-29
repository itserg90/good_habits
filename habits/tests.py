import time

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from habits.models import Habit
from users.models import User


class HabitTestCase(APITestCase):
    maxDiff = None

    def setUp(self):
        self.user = User.objects.create(email="admin@test.ru", tg_chat_id="1")
        self.habit_2 = Habit.objects.create(
            action="habit_test_2",
            place="Улица",
            user=self.user,
            time=time.strftime("%H:%M:%S", (2024, 1, 1, 14, 00, 00, 0, 0, 0)),
            pleasant_habit=True,
        )
        self.habit_1 = Habit.objects.create(
            action="habit_test_1",
            place="Дом",
            user=self.user,
            time=time.strftime("%H:%M:%S", (2024, 1, 1, 14, 00, 00, 0, 0, 0)),
            publicity=True,
            time_to_complete="00:01:40",
            related_habit=self.habit_2,
        )
        self.client.force_authenticate(user=self.user)

    def test_habit_create(self):
        url = reverse("habits:habit_create")
        data = {
            "action": "habit_test_3",
            "place": "Бассейн",
            "time": time.strftime("%H:%M:%S", (2024, 1, 1, 14, 00, 00, 0, 0, 0)),
            "related_habit": self.habit_2.pk,
            "user": self.user.pk,
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Habit.objects.count(), 3)

    def test_habit_update(self):
        url = reverse("habits:habit_update", args=(self.habit_1.pk,))
        data = {"action": "habit_test_1_updated"}
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("action"), "habit_test_1_updated")

    def test_habit_delete(self):
        url = reverse("habits:habit_delete", args=(self.habit_1.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Habit.objects.count(), 1)

    def test_habit_list(self):
        url = reverse("habits:habit_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()["results"]), 2)
        data = response.json()
        updated_at_1 = self.habit_1.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
        updated_at_2 = self.habit_2.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
        result = {
            "count": 2,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": self.habit_2.id,
                    "place": self.habit_2.place,
                    "time": self.habit_2.time,
                    "action": self.habit_2.action,
                    "pleasant_habit": self.habit_2.pleasant_habit,
                    "periodicity": self.habit_2.periodicity,
                    "reward": self.habit_2.reward,
                    "time_to_complete": self.habit_2.time_to_complete,
                    "publicity": self.habit_2.publicity,
                    "updated_at": updated_at_2,
                    "user": self.habit_2.user.id,
                    "related_habit": self.habit_2.related_habit,
                },
                {
                    "id": self.habit_1.id,
                    "place": self.habit_1.place,
                    "time": self.habit_1.time,
                    "action": self.habit_1.action,
                    "pleasant_habit": self.habit_1.pleasant_habit,
                    "periodicity": self.habit_1.periodicity,
                    "reward": self.habit_1.reward,
                    "time_to_complete": self.habit_1.time_to_complete,
                    "publicity": self.habit_1.publicity,
                    "updated_at": updated_at_1,
                    "user": self.habit_1.user.id,
                    "related_habit": self.habit_1.related_habit.pk,
                },
            ],
        }
        self.assertEqual(data, result)

    def test_public_habit_list(self):
        url = reverse("habits:public_habit_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()["results"]), 1)
        data = response.json()
        updated_at_1 = self.habit_1.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
        result = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": self.habit_1.id,
                    "place": self.habit_1.place,
                    "time": self.habit_1.time,
                    "action": self.habit_1.action,
                    "pleasant_habit": self.habit_1.pleasant_habit,
                    "periodicity": self.habit_1.periodicity,
                    "reward": self.habit_1.reward,
                    "time_to_complete": self.habit_1.time_to_complete,
                    "publicity": self.habit_1.publicity,
                    "updated_at": updated_at_1,
                    "user": self.habit_1.user.id,
                    "related_habit": self.habit_1.related_habit.pk,
                }
            ],
        }
        self.assertEqual(data, result)
