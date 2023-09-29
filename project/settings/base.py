"""Base Configuration File."""

import os
from project.core_settings import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY")

INSTALLED_APPS += [
    "rest_framework",
    "corsheaders",
    "rest_framework_filters",
    "dj_rest_auth",
    "task_manager",
    "rest_framework.authtoken",
]

SITE_ID = 1

REST_AUTH = {
    "USE_JWT": True,
    "OLD_PASSWORD_FIELD_ENABLED": True,
    "LOGOUT_ON_PASSWORD_CHANGE": False,
    "REST_AUTH_TOKEN_MODEL": None,
    "USER_DETAILS_SERIALIZER": "task_manager.serializers.core.UserSerializer",
    "JWT_TOKEN_CLAIMS_SERIALIZER": "task_manager.serializers.core.JWTTokenSerializer",
    "JWT_SERIALIZER": "task_manager.serializers.core.JWTSerializer",
}

AUTHENTICATION_BACKENDS = ("django.contrib.auth.backends.ModelBackend",)
