from django.urls import path
from rest_framework.permissions import AllowAny
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from users.apps import UsersConfig
from users.views import PaymentsViewSet, UserCreateAPIView, UserDestroyApiView, UserUpdateApiView, UserRetrieveApiView

app_name = UsersConfig.name


urlpatterns = [
    path("register/", UserCreateAPIView.as_view(), name="register"),
    path(
        "login",
        TokenObtainPairView.as_view(permission_classes=(AllowAny,)),
        name="login",
    ),
    path(
        "token/refresh",
        TokenRefreshView.as_view(permission_classes=(AllowAny,)),
        name="token_refresh",
    ),
    path("users/<int:pk>", UserRetrieveApiView.as_view(), name='user-detail'),
    path("users/<int:pk>/update", UserUpdateApiView.as_view(), name='user-update'),
    path("users/<int:pk>/delete", UserDestroyApiView.as_view(), name='user-delete'),
]
