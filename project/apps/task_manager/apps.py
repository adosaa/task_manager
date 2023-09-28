from __future__ import unicode_literals
from django.apps import AppConfig

# =======================================
# Do what needs to be doen in APP config.
# This is a good place to import signals
# =======================================


class TaskManagerAppConfig(AppConfig):
    name = "task_manager"

    # # If there are signals to be processed (for DB triggers, refer them here)
    def ready(self):
        """."""
