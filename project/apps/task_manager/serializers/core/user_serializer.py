"""
User Serializer.

Part of serializers.core module.
"""

__license__ = "MIT"
__version__ = "0.0.1"
__author__ = "Ariel Saavedra D."
__email__ = "adosaa@gmail.com"
__copyright__ = "Copyright 2023, TaskManager."

from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer class for django.contrib.User core Model.

    :@param {all} all - all the User fields serialized.
    :@raises {None}
    :@returns {None}
    """

    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "is_staff",
        )
        read_only_fields = ("id",)
