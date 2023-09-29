"""
CustomTokenRefresh Serializer.

Part of serializers.core module.
"""

__license__ = "MIT"
__version__ = "0.0.1"
__author__ = "Ariel Saavedra D."
__email__ = "adosaa@gmail.com"
__copyright__ = "Copyright 2023, TaskManager."


from dj_rest_auth.utils import jwt_encode
from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework_simplejwt.tokens import AccessToken


class CustomTokenRefreshSerializer(serializers.Serializer):
    """
    CustomTokenRefresh Serializer method.

    An override of the refresh serializer method for simplejwt.
    Developed for working with only access token types.
    """

    token = serializers.CharField()

    def validate(self, attrs):
        """
        validate method.

        Checks if access token provided is valid and then
        issues a new token.

        Args:
            attrs (str): view input payload.

        Raises:
            Exception: TokenError.

        Returns:
            dict: dictionary with access token as attr.
        """
        token = AccessToken(attrs["token"])
        token.verify()

        user = User.objects.get(id=token.payload["user_id"])
        # Issue new token
        new_access_token = jwt_encode(user)[0]
        data = {"access": str(new_access_token)}

        return data
