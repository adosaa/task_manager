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
    A model to store Core Task instances.

    :@attr {UUID} id - unique identification for the instance/record (inherited from BaseModel).
    :@attr {Boolean} is_active - state (inactive/active) of the record (inherited from BaseModel).
    :@attr {bool} is_deleted - state (removed/Not-removed) of the record (inherited from BaseModel).
    :@attr {string} created_by - string with the username which created the record
        (inherited from BaseModel).
    :@attr {datetime} created_at - date and time of the record creation (inherited from BaseModel).
    :@attr {datetime} updated_at - date and time of the record edition (inherited from BaseModel).
    :@attr {Dict} extra_fields - an extra JSONField for non-migrations and expansion purposes.
    (inherited from BaseModel).
    :@attr {EconomicCategory} economic_categories - ManyToMany EconomicCategory ForeignKey
        reference.
    :@attr {Dict} extra_fields - an extra JSONField for non-migrations and expansion purposes
    (inherited from BaseModel).
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
