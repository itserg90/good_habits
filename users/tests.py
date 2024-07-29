from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from users.models import User


class HabitTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email="admin@test.ru")
        self.user.set_password("123qwe")
        self.client.force_authenticate(user=self.user)

    def test_user_create(self):
        url = reverse("users:register")
        data = {"email": "admin2@test.ru", "password": "123qwe"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 2)

    def test_user_update(self):
        url = reverse("users:user_update", args=(self.user.pk,))
        data = {"email": "admin_updated@test.ru"}
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("email"), "admin_updated@test.ru")
