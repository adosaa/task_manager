"""
TaskEnum.

Part of enums module.
"""

__license__ = "MIT"
__version__ = "0.0.1"
__author__ = "Ariel Saavedra D"
__email__ = "adosaa@gmail.com"
__copyright__ = "Copyright 2023, TaskManager."


class TaskEnum(object):
    """
    TaskEnum Class.

    A class to save all possible statuses of Task instances.

    Attr:
        pending (int): unique integer id representing a task without beginning.
        in_progress (int): unique integer ID representing a task in the process
        of being done.
        complete (int): unique integer id representing an finished task.
        task_statuses (dict): dictionary which group by all the previous task
        states in one tuple.
    """

    pending = 0
    in_progress = 1
    completed = 2

    task_statuses = (
        (pending, "PENDING"),
        (in_progress, "IN_PROGRESS"),
        (completed, "COMPLETED"),
    )
