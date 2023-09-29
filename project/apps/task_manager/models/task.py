"""
Task Model.

Part of models module.
"""

__license__ = "MIT"
__version__ = "0.0.1"
__author__ = "Ariel Saavedra D"
__email__ = "adosaa@gmail.com"
__copyright__ = "Copyright 2023, TaskManager."

from django.db import models
from task_manager.enums import TaskEnum
from task_manager.models import BaseModel


class Task(BaseModel):
    """
    Task Model.

    A model to store Task instances.

    Attr:
        id (str, UUID): unique identification for the instance/record.
        created_at (datetime): date and time of the record creation.
        updated_at (datetime): date and time of the record edition.
        created_by (str): tring with the username which created the
        record.
        extra_fields (dict): an extra JSONField for non-migrations
        and expansion purposes.
        is_active (bool): state (inactive/active) of the record.
        is_deleted (bool): state (removed/Not-removed) of the record.

        title (str): summary of a task.
        description (str): detail of a task.
        due_date (datetime.date): time mark when a task should be
        finished or out of date.
        status (int): possible options in which a task is present
        currently. 

    Returns:
        Task: Task instance.
    """

    title = models.CharField(max_length=350, blank=False, null=False, default="")
    description = models.TextField(null=False, blank=False)
    due_date = models.DateField(blank=False, null=False)
    status = models.IntegerField(
        choices=TaskEnum.task_statuses,
        blank=False,
        null=False,
        default=TaskEnum.pending,
    )

    def __str__(self):
        """
        __str__ method.

        String representation of Task.
        """
        return "%s - %s" % (self.title, self.due_date)

    class Meta:
        """
        Meta Class.

        Metadata options for Task.
        """

        verbose_name_plural = "tasks"
        app_label = "task_manager"
