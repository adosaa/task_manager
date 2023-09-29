from django.urls import path, include
from task_manager.routers.task import urls as task_urls

urlpatterns = [
    path("task/", include(task_urls)),
]
