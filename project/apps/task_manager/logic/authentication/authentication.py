"""
AuthenticatedServiceClient & JWTServiceOnlyAuthentication Classes.

Part of logic.authentication module.
"""

__license__ = "MIT"
__version__ = "0.0.1"
__author__ = "Ariel Saavedra D"
__email__ = "adosaa@gmail.com"
__copyright__ = "Copyright 2023, TaskManager."

from rest_framework_simplejwt.authentication import JWTAuthentication


class AuthenticatedServiceClient:
    """
    AuthenticatedServiceClient Class.

    This acts as a in-memory (partial) user object that is built from the token data.
    """

    def __init__(self, payload):
        """
        __init__ method.

        Constructor of AuthenticatedServiceClient.
        """
        self.payload = payload
        self.is_active = True
        self.is_authenticated = True
        self.is_staff = payload.get("is_staff")
        self.username = payload.get("username")


class JWTServiceOnlyAuthentication(JWTAuthentication):
    """
    JWTServiceOnlyAuthentication Class.

    Enhancement to JSONWebTokenAuthentication class which without usermodel.

    A in-memory (partial) user object is created to act as a proxy.
    """

    def authenticate_credentials(self, payload):
        """
        Get a parsed version of the user info for transversal between systems purposes.

        Args:
            payload (dict): info of the logged user from the token parsing mechanism.

        Returns:
            client (Class): Class with attributes of the logged user.
        """
        client = AuthenticatedServiceClient(payload)
        return client
