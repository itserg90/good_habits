from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractUser):
    username = None

    email = models.EmailField(
        unique=True, verbose_name="Почта", help_text="Укажите почту"
    )

    phone = PhoneNumberField(
        verbose_name="Телефон",
        blank=True,
        null=True,
        help_text="Введите номер телефона",
    )
    city = models.CharField(
        verbose_name="Город", blank=True, null=True, help_text="Введите город"
    )
    avatar = models.ImageField(
        upload_to="users/avatars/",
        verbose_name="Аватар",
        blank=True,
        null=True,
        help_text="Загрузите изображение",
    )
    tg_chat_id = models.CharField(
        max_length=50,
        verbose_name="Телеграм chat_id",
        blank=True,
        null=True,
        help_text="Укажите телеграм chat_id",
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email
