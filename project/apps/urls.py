from django.urls import path, include
from rest_framework_simplejwt.views import token_refresh, token_verify

urlpatterns = [
    path("api/v1/", include("task_manager.urls")),
    path("auth/", include("dj_rest_auth.urls")),
    path("refresh_token/", token_refresh),
    path("verify_token/", token_verify),
]
