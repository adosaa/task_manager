"""
Task Serializer.

Part of serializers module.
"""

__license__ = "MIT"
__version__ = "0.0.1"
__author__ = "Ariel Saavedra D"
__email__ = "adosaa@gmail.com"
__copyright__ = "Copyright 2023, TaskManager."


from drf_dynamic_fields import DynamicFieldsMixin
from rest_framework import serializers

from task_manager.enums import TaskEnum
from task_manager.models.task import Task


class TaskSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    """
    Serializer class for UserProattached_file core Model.

    :@param {all} all - all the Task fields serialized.
    :@raises {None}
    :@returns {None}
    """

    title = serializers.CharField(required=True, allow_null=False)
    description = serializers.CharField(required=True, allow_null=True)
    status = serializers.CharField(required=True, allow_null=False)
    due_date = serializers.DateField(required=True, allow_null=False)
    status_str = serializers.SerializerMethodField(read_only=True)

    def validate_status(self, value):
        """_summary_

        Args:
            value (_type_): _description_

        Raises:
            serializers.ValidationError: _description_

        Returns:
            _type_: _description_
        """
        status = value if value is not None else None
        is_status_valid = False
        try:
            is_status_valid = (
                True
                if int(status) in [task_type[0] for task_type in TaskEnum.task_statuses]
                else False
            )
        except Exception:
            is_status_valid = (
                True if status in [task_type[1] for task_type in TaskEnum.task_statuses] else False
            )
            for task_type in TaskEnum.task_statuses:
                if task_type[1] == status:
                    status = task_type[0]
        if is_status_valid:
            return status
        else:
            raise serializers.ValidationError("Not valid status")

    def get_status_str(self, obj):
        """_summary_

        Args:
            obj (_type_): _description_

        Returns:
            _type_: _description_
        """
        status_str = str()
        try:
            for task_type in TaskEnum.task_statuses:
                if int(obj.status) in task_type:
                    status_str = task_type[1]
                    break
        except Exception:
            status_str = ""
        finally:
            return status_str

    class Meta:
        """Metadata options for Task Serializer."""

        model = Task
        fields = ("id", "created_by", "title", "description", "due_date", "status", "status_str")
