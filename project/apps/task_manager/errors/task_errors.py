"""
Task error's list.

part of errors module.
"""

__license__ = "MIT"
__version__ = "0.0.1"
__author__ = "Ariel Saavedra D"
__email__ = "adosaa@gmail.com"
__copyright__ = "Copyright 2023, TaskManager."

from rest_framework.exceptions import APIException


class TaskInternalError(APIException):
    status_code = 500
    default_detail = "Server for accessing Task API not available, try again later."
    default_code = "task_server_error"
    message = ""


class TaskNotFound(APIException):
    status_code = 404
    default_detail = "Task record not found"
    default_code = "task_not_found"
    message = ""


class TaskUnauthorized(APIException):
    status_code = 401
    default_detail = "Unauthorized use of Task resources"
    default_code = "task_unauthorized"
    message = ""


class TaskBadRequest(APIException):
    status_code = 400
    default_detail = "Malformed request in Task operations"
    default_code = "task_bad_request"
    message = ""


class TaskInternalBadRequest(APIException):
    status_code = 400
    default_detail = "Malformed request in Task operations"
    default_code = "task_bad_request"
    message = ""


class TaskDuplicte(APIException):
    status_code = 400
    default_detail = "Task already exists in the system."
    default_code = "task_duplicate_request_intent"
    message = ""


class TaskForbidden(APIException):
    status_code = 403
    default_detail = "Invalid Task ID for this type of user creation."
    default_code = "task_forbidden"
    message = ""
