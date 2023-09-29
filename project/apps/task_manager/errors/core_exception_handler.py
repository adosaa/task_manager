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
    """_summary_

    Args:
        exc (_type_): _description_
        context (_type_): _description_

    Returns:
        _type_: _description_
    """
    response = exception_handler(exc, context)
    if response is not None:
        response.data["status_code"] = response.status_code
        response.data["default_detail"] = exc.default_detail
        response.data["default_code"] = exc.default_code

    return response
