"""
CustomTokenVerify Serializer.

Part of serializers.core module.
"""

__license__ = "MIT"
__version__ = "0.0.1"
__author__ = "Ariel Saavedra D."
__email__ = "adosaa@gmail.com"
__copyright__ = "Copyright 2023, TaskManager."


from rest_framework import serializers
from rest_framework_simplejwt.tokens import AccessToken


class CustomTokenVerifySerializer(serializers.Serializer):
    """
    CustomTokenVerify Serializer method.

    An override of the verify serializer method for simplejwt.
    Developed for working with only access token types.

    :@attr {String} token - token input as string.
    :@raises {TokenError}
    :@returns {dict} - dictionary with access token as attr.
    """

    token = serializers.CharField()

    def validate(self, attrs):
        """
        validate method.
        Checks if access token provided in payload is valid.

        :@attr {String} - view input payload.
        :@raises {TokenError}
        :@returns {dict} - dictionary with access token as attr.
        """
        token = AccessToken(attrs["token"])
        token.verify()
        data = {"token": str(token)}

        return data
