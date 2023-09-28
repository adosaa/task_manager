"""
JWT Serializer.

Part of serializers.core module.
"""

__license__ = "MIT"
__version__ = "0.0.1"
__author__ = "Ariel Saavedra D."
__email__ = "adosaa@gmail.com"
__copyright__ = "Copyright 2023, TaskManager."


from django.conf import settings
from django.utils.module_loading import import_string
from rest_framework import serializers


class JWTSerializer(serializers.Serializer):
    """
    Serializer customization for JWT authentication.

    :@param {all} all - all the token fields serialized.
    :@raises {None}
    :@returns {None}
    """

    token = serializers.CharField(source="access_token")
    user = serializers.SerializerMethodField()

    def get_user(self, obj):
        """
        Serializer method field for obtaining user information.
        Uses USER_DETAILS_SERIALIZER declared in settings.

        :@param {Token} - jwt object.
        :@raises {None}
        :@returns {JWTUserDetailsSerializer}
        """
        rest_auth_serializers = getattr(settings, "REST_AUTH", {})

        JWTUserDetailsSerializer = import_string(
            rest_auth_serializers.get(
                "USER_DETAILS_SERIALIZER",
                "dj_rest_auth.serializers.UserDetailsSerializer",
            ),
        )
        user_data = JWTUserDetailsSerializer(obj["user"], context=self.context).data
        return user_data
