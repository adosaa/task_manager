from datetime import date
from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.test import APIRequestFactory, force_authenticate
from rest_framework_simplejwt.tokens import RefreshToken

from task_manager.models import Task
from task_manager.views import TaskView


class TestTaskView(TestCase):
    """Test View Task."""

    def setUp(self):
        """Initialize test."""

        self.factory = APIRequestFactory()
        # Create a user
        User.objects.create_user(
            username="asaavedra",
            email="adosaa@gmail.com",
            password="dk5c+Pu!E%9jmMK-",
        )
        self.user = User.objects.get(username="asaavedra")
        self.user.is_staff = True
        self.user.save()

        # Create Access Token for user
        self.token_data = RefreshToken().for_user(self.user).access_token
        self.token_data["username"] = self.user.username
        self.token_data["is_staff"] = True

        self.global_endpoints = TaskView.as_view(actions={"get": "list", "post": "create"})
        self.unitary_endpoint = TaskView.as_view(
            actions={"get": "retrieve", "patch": "partial_update", "delete": "destroy"}
        )

    def test_create_task_via_endpoint(self):
        """Test Create should succeed."""
        data = None
        # Post body params
        body = {
            "title": "tareas",
            "description": "matematicas",
            "due_date": "2023-09-28",
            "status": "IN_PROGRESS",
        }
        # Process endpoint - Create task
        request = self.factory.post(
            "api/v1/task/?format=json",
            body,
        )
        force_authenticate(request, user=self.user, token=self.token_data)

        response = self.global_endpoints(request)
        data = response.data

        # Assertions
        self.assertEqual(response.status_code, 201)
        self.assertTrue(isinstance(data, dict))

    def test_update_task_via_endpoint(self):
        """Test Edit should succeed."""
        data = None
        # Post body params
        task = Task.objects.create(
            title="tareas", description="matematicas", due_date=date(2023, 9, 28), status=1
        )
        body = {"status": "COMPLETED"}
        # Process endpoint - Update task status
        request = self.factory.patch(
            "api/v1/task/%s?format=json" % (str(task.id)),
            body,
        )
        force_authenticate(request, user=self.user, token=self.token_data)

        response = self.unitary_endpoint(request, pk=str(task.id))
        data = response.data

        # Assertions
        self.assertEqual(response.status_code, 200)
        self.assertTrue(isinstance(data, dict))
        self.assertEqual(data["id"], str(task.id))
        self.assertEqual(data["status"], "2")

    def test_delete_task_via_endpoint(self):
        """Test delete should succeed."""
        # Post body params
        task = Task.objects.create(
            title="tareas #2", description="lenguaje", due_date=date(2023, 9, 28), status=1
        )
        body = {"status": "COMPLETED"}
        # Process endpoint - delete task
        request = self.factory.delete(
            "api/v1/task/%s?format=json" % (str(task.id)),
            body,
        )
        force_authenticate(request, user=self.user, token=self.token_data)

        response = self.unitary_endpoint(request, pk=str(task.id))

        # Assertions
        self.assertEqual(response.status_code, 204)

    def test_retrieve_task_via_endpoint(self):
        """Test retrieve instance should succeed."""
        data = None
        # Post body params
        task = Task.objects.create(
            title="tareas #3", description="Historia", due_date=date(2023, 9, 28), status=1
        )
        body = {"status": "COMPLETED"}
        # Process endpoint - retriene unitary task
        request = self.factory.get(
            "api/v1/task/%s?format=json" % (str(task.id)),
            body,
        )
        force_authenticate(request, user=self.user, token=self.token_data)

        response = self.unitary_endpoint(request, pk=str(task.id))
        data = response.data

        # Assertions
        self.assertEqual(response.status_code, 200)
        self.assertTrue(isinstance(data, dict))
        self.assertEqual(data["id"], str(task.id))
        self.assertEqual(data["status"], "1")

    def test_retrieve_collection_task_via_endpoint(self):
        """Test retrieve all task collection should succeed."""
        data = None
        # Post body params
        task = Task.objects.create(
            title="tareas #1", description="Historia", due_date=date(2023, 9, 28), status=1
        )
        task2 = Task.objects.create(
            title="tareas #2", description="Fisica", due_date=date(2023, 9, 28), status=0
        )
        task3 = Task.objects.create(
            title="tareas #3", description="Quimica", due_date=date(2023, 9, 28), status=0
        )
        # Process endpoint - retrieve task collection
        request = self.factory.get("api/v1/task/?format=json")
        force_authenticate(request, user=self.user, token=self.token_data)

        response = self.global_endpoints(request)
        data = response.data

        # Assertions
        self.assertEqual(response.status_code, 200)
        self.assertTrue(isinstance(data, dict))
        self.assertEqual(len(data["results"]), 3)
        self.assertEqual(data["results"][0]["id"], str(task3.id))
        self.assertEqual(data["results"][1]["id"], str(task2.id))
        self.assertEqual(data["results"][2]["id"], str(task.id))
