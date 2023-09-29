"""Development Environment Configuration File."""

import os
from project.settings.base import *

DEBUG = True
TEMPLATES[0]["OPTIONS"]["debug"] = DEBUG

ALLOWED_HOSTS = [
    ".execute-api.us-east-1.amazonaws.com",
    ".amplifyapp.com"
]

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

CORS_ORIGIN_REGEX_WHITELIST = (
    r"^(https?:\/\/)?(\w+\.)?localhost(:8000)?$",
    r"^(http?:\/\/)?(\w+\.)?localhost(:8080)?$",
    r"^(http?:\/\/)?(\w+\.)?127.0.0.1(:8080)?$",
    r"^(https?:\/\/)?development.?(\w+\.)?amplifyapp\.com$",
)

SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = "DENY"
SECURE_HSTS_SECONDS = 2592000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

PERMISSIONS_POLICY = {
    "accelerometer": [],
    "ambient-light-sensor": [],
    "autoplay": [],
    "camera": [],
    "document-domain": [],
    "encrypted-media": [],
    "fullscreen": [],
    "geolocation": [],
    "gyroscope": [],
    "magnetometer": [],
    "microphone": [],
    "midi": [],
    "payment": [],
    "sync-xhr": [],
    "usb": [],
}

SIMPLE_JWT["ACCESS_TOKEN_LIFETIME"] = datetime.timedelta(hours=2)
SIMPLE_JWT["REFRESH_TOKEN_LIFETIME"] = datetime.timedelta(hours=2)