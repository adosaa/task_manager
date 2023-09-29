"""
Core HTTP Exception handler method.

part of errors module.
"""

__license__ = "MIT"
__version__ = "0.0.1"
__author__ = "Ariel Saavedra D"
__email__ = "adosaa@gmail.com"
__copyright__ = "Copyright 2023, TaskManager."

from rest_framework.views import exception_handler


def core_exception_handler(exc, context):
    """
    core_exception_handler method.

    Handler which decores a common exception in APIException type format.

    Args:
        exc (Exception): Exception Python class.
        context (dict): Serializer's View context.

    Returns:
        response (APIException): A class composed of attributes like
        status_code, default_detail, default_code and, message.
    """
    response = exception_handler(exc, context)
    if response is not None:
        response.data["status_code"] = response.status_code
        response.data["default_detail"] = exc.default_detail
        response.data["default_code"] = exc.default_code

    return response
