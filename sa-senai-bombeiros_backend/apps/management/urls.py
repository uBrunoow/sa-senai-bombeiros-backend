from apps.management import api
from django.urls import include, path
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"user", api.UserViewSet)
router.register(r"admin", api.AdminViewSet)
router.register(r"register-admin", api.AdminRegister, basename="register-admin")
router.register(r"register-firefighter", api.FirefighterRegister, basename="register-firefighter")
router.register(r"firefighter", api.FirefighterViewSet)

urlpatterns = [
    path("logout/", api.LogoutView.as_view()),
    path(
        "change_password/<uuid:pk>/",
        api.UserChangePasswordView.as_view(),
        name="auth_change_password",
    ),
    path("", include(router.urls)),
    path(
        "password_reset/",
        include("django_rest_passwordreset.urls", namespace="password_reset"),
    ),
]