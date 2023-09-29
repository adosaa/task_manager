"""
JWT Serializer.

Part of serializers.core module.
"""

__license__ = "MIT"
__version__ = "0.0.1"
__author__ = "Ariel Saavedra D."
__email__ = "adosaa@gmail.com"
__copyright__ = "Copyright 2023, TaskManager."


from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class JWTTokenSerializer(TokenObtainPairSerializer):
    """
    JWTTokenSerializer class.

    Serializer customization for JWT Token claims.
    """

    @classmethod
    def get_token(cls, user):
        """
        get_token method.

        Used for assigning extra claims to token object.

        Args:
            user (User): User model instance.

        Raises:
            None

        Returns:
            dict: Updated token instance of corresponding token class.
        """
        token = super().get_token(user)

        token["username"] = user.username
        token["is_staff"] = user.is_staff
        token["is_sudo"] = user.is_superuser
        token["email"] = user.email
        return token
