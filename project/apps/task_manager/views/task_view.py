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

    :@attr {Model Class} model_class - model class of the view
    :@attr {queryset instance} queryset - general queryset from the model
    :@attr {Serializer Class} serializer_class - serializer model of the view
    :@attr {tuple} permission_classes - tuple with all general DRF permissions of the view
    :@attr {Class} filter_class - sub class which filters record/collection of the Task entity
        by their fields.
    :@raises {None}
    :@returns {None}
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
        self.ordering_fields = "__all__"
        self.filter_backends = (RestFrameworkFilterBackend, OrderingFilter, SearchFilter)
        self.search_fields = "title"
        self.ordering = ("-created_at",)

    def retrieve(self, request, pk, *args, **kwargs):
        """
        GET (retrive instance) method.

        Using TaskView.get_object_with_params method for geting only
        one Task instances.

        :@params {tuple} request - HTTP request object from the frontend/user
        side.
        :@params {string} pk - Task instance ID to modify.
        :@raises {APIException}
        :@returns {Task instance} single record of Task model.
        """
        try:
            return super(viewsets.ModelViewSet, self).retrieve(request, *args, **kwargs)
        except Exception:
            raise TaskNotFound({"message": f"{pk} not found or valid"})

    def list(self, request, *args, **kwargs):
        """
                GET (collection list) method.
        COMPLETED
                :@params {tuple} request - HTTP request object from the frontend/user side.
                :@raises {APIException}
                :@returns {Task} list of all Task instances.
        """
        try:
            return super(viewsets.ModelViewSet, self).list(request, *args, **kwargs)
        except Exception as e:
            raise TaskInternalError({"message": str(e)})

    def create(self, request, *args, **kwargs):
        """
        POST (create instance) method.

        :@params {tuple} request - HTTP request object from the frontend/user side.
        :@raises {APIException}
        :@returns {Task} created Task instance.
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
        PATCH (edit instance) method.

        :@params {tuple} request - HTTP request object from the frontend/user side.
        :@params {String} pk - Task instance ID.
        :@raises {APIException}
        :@returns {Task} Edited Task instance.
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
        DELETE (edit instance) method.

        :@params {tuple} request - HTTP request object from the frontend/user side.
        :@params {String} pk - Task instance ID.
        :@raises {APIException}
        :@returns HTTP_204_NO_CONTENT
        """
        try:
            return super(viewsets.ModelViewSet, self).destroy(request, *args, **kwargs)
        except Exception:
            raise TaskNotFound({"message": f"{pk} not found or valid"})
