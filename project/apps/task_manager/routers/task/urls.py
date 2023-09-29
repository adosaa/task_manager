"""
Task router urls.

Part of routers.task module.
"""

__license__ = "MIT"
__version__ = "0.0.1"
__author__ = "Ariel Saavedra D"
__email__ = "adosaa@gmail.com"
__copyright__ = "Copyright 2023, TaskManager."


from django.urls import path
from task_manager.views import TaskView

urlpatterns = [
    path(
        "",
        TaskView.as_view(
            {
                "get": "list",
                "post": "create",
            }
        ),
        name="task",
    ),
    path(
        "<slug:pk>",
        TaskView.as_view({"get": "retrieve", "patch": "partial_update", "delete": "destroy"}),
        name="task_detail",
    ),
]
