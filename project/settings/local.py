"""Local Environment Configuration File."""

import os
from project.settings.base import *

DEBUG = True
TEMPLATES[0]["OPTIONS"]["debug"] = DEBUG

ALLOWED_HOSTS = [".local", ".test", "127.0.0.1", ".localhost"]

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases
DATABASES = {
    "default": {
        "ENGINE": os.getenv("DB_ENGINE"),
        "NAME": os.getenv("DB_NAME"),
        "USER": os.getenv("DB_USER"),
        "PASSWORD": os.getenv("DB_PASSWORD"),
        "HOST": os.getenv("DB_HOST"),
        "PORT": os.getenv("DB_PORT"),
    }
}

CSRF_COOKIE_SECURE = False
CSRF_COOKIE_HTTPONLY = False

CORS_ORIGIN_REGEX_WHITELIST = (
    r"^(https?:\/\/)?(\w+\.)?localhost(:8000)?$",
    r"^(http?:\/\/)?(\w+\.)?localhost(:8080)?$",
    r"^(http?:\/\/)?(\w+\.)?127.0.0.1(:8080)?$",
    r"^(https?:\/\/)?development.?(\w+\.)?amplifyapp\.com$",
)
