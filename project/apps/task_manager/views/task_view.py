"""
Task View class.

Part of views module.
"""

__license__ = "MIT"
__version__ = "0.0.1"
__author__ = "Ariel Saavedra D"
__email__ = "adosaa@gmail.com"
__copyright__ = "Copyright 2023, TaskManager."

import copy

from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_filters.backends import RestFrameworkFilterBackend

from task_manager.errors.task_errors import TaskBadRequest, TaskInternalError, TaskNotFound
from task_manager.models import Task
from task_manager.serializers import TaskSerializer


class TaskView(viewsets.ModelViewSet):
    """
    TaskView View Class.

    Principal class in charge of maintaining CRUD operations logic.

    Attr:
        model_class (Task): model class of the view.
        queryset (Queryset instance): general queryset from the model.
        serializer_class (TaskSerializer): serializer class of the view.
        permission_classes (tuple): tuple with all general DRF permissions
        of the view.
        filter_backends (tuple): tuple with all general DRF filter classes
        available for the view.
        search_fields (list): fields for lookup.
        ordering (tuple): fields that mark the collection's order by default.
    """

    def __init__(self):
        """
        __init__ method.

        Constructor of TaskView.
        """
        self.model_class = Task
        self.queryset = Task.objects.all()
        self.serializer_class = TaskSerializer
        self.permission_classes = (IsAuthenticated,)
        self.filter_backends = (RestFrameworkFilterBackend, OrderingFilter, SearchFilter)
        self.search_fields = ["=created_by"]
        self.ordering = ("-created_at",)

    def retrieve(self, request, pk, *args, **kwargs):
        """
        retrieve method (GET).

        EP representation used for getting only one Task instance.

        Args:
            request (dict): HTTP request object from the frontend/user
            side.
            pk (str): Task instance ID.

        Raises:
            APIException: HTTP error in EP execution.

        Returns:
            Task (JSON representation): single record of Task model.
        """
        try:
            return super(viewsets.ModelViewSet, self).retrieve(request, *args, **kwargs)
        except Exception:
            raise TaskNotFound({"message": f"{pk} not found or valid"})

    def list(self, request, *args, **kwargs):
        """
        list method (GET).

        EP representation used for getting a Task collection.

        Args:
            request (dict): HTTP request object from the frontend/user
            side.

        Raises:
            APIException: HTTP error in EP execution.

        Returns:
            Task List (list): set or subset of Task's collection.
        """
        try:
            return super(viewsets.ModelViewSet, self).list(request, *args, **kwargs)
        except Exception as e:
            raise TaskInternalError({"message": str(e)})

    def create(self, request, *args, **kwargs):
        """
        create method (POST).

        EP representation used for creating a Task instance.

        Args:
            request (dict): HTTP request object from the frontend/user
            side.

        Raises:
            APIException: HTTP error in EP execution.

        Returns:
            Task (JSON representation): created Task instance.
        """
        try:
            token_data = request.auth
            task_body = copy.deepcopy(request.data)
            task_body["created_by"] = token_data.get("username", "")
            serializer = self.serializer_class(data=task_body)
            if not serializer.is_valid():
                raise TaskBadRequest({"message": serializer.errors})
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        except Exception as e:
            raise e

    def partial_update(self, request, pk, *args, **kwargs):
        """
        partial_update method (PATCH).

        EP representation used for editing certain parts of a
        Task instance.

        Args:
            request (dict): HTTP request object from the frontend/user
            side.
            pk (str): Task instance ID.

        Raises:
            APIException: HTTP error in EP execution.

        Returns:
            Task (JSON representation): single record of edited Task.
        """
        try:
            task_instance = get_object_or_404(self.model_class, pk=pk)
            serializer = self.serializer_class(task_instance, data=request.data, partial=True)
            if not serializer.is_valid():
                raise TaskBadRequest({"message": serializer.errors})
            serializer.save()
            return Response(serializer.data, status.HTTP_200_OK)
        except Exception as e:
            raise e

    def delete(self, request, pk, *args, **kwargs):
        """
        delete method (DELETE).

        EP representation used for delete a Task instance.

        Args:
            request (dict): HTTP request object from the frontend/user
            side.
            pk (str): Task instance ID.

        Raises:
            APIException: HTTP error in EP execution.

        Returns:
            None (HTTP 204 status): HTTP signaling success in the operation.
        """
        try:
            return super(viewsets.ModelViewSet, self).destroy(request, *args, **kwargs)
        except Exception:
            raise TaskNotFound({"message": f"{pk} not found or valid"})
