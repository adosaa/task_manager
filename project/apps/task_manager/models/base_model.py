"""
BaseModel Model.

Part of models module.
"""

__license__ = "MIT"
__version__ = "0.0.1"
__author__ = "Ariel Saavedra D"
__email__ = "adosaa@gmail.com"
__copyright__ = "Copyright 2023, TaskManager."


import uuid
from django.db.models import JSONField
from django.db import models


class BaseModel(models.Model):
    """
    BaseModel abstract model Class.

    An abstract model with all the basic fields for each table in the system.

    :@attr {UUID} id - unique identification for the instance/record.
    :@attr {datetime} created_at - date and time of the record creation.
    :@attr {datetime} updated_at - date and time of the record edition.
    :@attr {string} created_by - string with the username which created the record.
    :@attr {dict} extra_fields - an extra JSONField for non-migrations and expansion purposes.
    :@attr {bool} is_active - state (inactive/active) of the record.
    :@attr {bool} is_deleted - state (removed/Not-removed) of the record.
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=255, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    extra_fields = JSONField(default=dict, blank=True)
    is_active = models.BooleanField(blank=False, null=False, default=True)
    is_deleted = models.BooleanField(blank=False, null=False, default=False)

    def __str__(self):
        """
        __str__ method.

        String representation of BaseModel.
        """
        return self.id

    class Meta:
        """Metadata options for BaseModel."""

        abstract = True
