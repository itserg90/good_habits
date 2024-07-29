from django.urls import path
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from users.apps import UsersConfig
from users.views import UserCreateAPIView, UserUpdateAPIView

app_name = UsersConfig.name
urlpatterns = [
    path("registeк/", UserCreateAPIView.as_view(), name="register"),
    path("<int:pk>/update/", UserUpdateAPIView.as_view(), name="user_update"),
    # Авторизация и получение токенов
    path(
        "login/",
        TokenObtainPairView.as_view(permission_classes=(AllowAny,)),
        name="login",
    ),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
