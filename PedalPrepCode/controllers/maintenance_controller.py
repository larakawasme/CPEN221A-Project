from models.maintenance_model import MaintenanceModel


class MaintenanceController:
    def __init__(self, maintenance_model: MaintenanceModel):
        """
        Summary: Initializes the controller with a reference to the MaintenanceModel.

        Precondition: maintenance_model is an instance of MaintenanceModel.
        """
        self.maintenance_model = maintenance_model

    def get_task_history(self) -> list[dict]:
        """
        Summary: Retrieves all maintenance tasks within allowed time window.

        Postcondition: Returns a list of task dictionaries (task name, last completed date, notes).
        """
        return self.maintenance_model.get_tasks()

    def get_upcoming_and_overdue_tasks(self) -> tuple[list[dict], list[dict]]:
        """
        Summary: Determines which tasks are upcoming and which are overdue.

        Postcondition: Returns two lists of task dictionaries: (overdue_tasks, upcoming_tasks)
        """
        overdue, upcoming = self.maintenance_model.get_upcoming_and_overdue_tasks()
        return overdue, upcoming

    def mark_task_completed(self, task_name: str, notes: str = "") -> tuple[bool, str]:
        """
        Summary: Marks a maintenance task as completed.

        Precondition: task_name is an existing task
        Postcondition: Updates model with current timestamp and optional notes. Returns True if successful.
                        Also returns str with status message.
        """
        return self.maintenance_model.complete_task(task_name, notes)

    def get_task_instructions(self, task_name: str) -> str:
        """
        Summary: Retrieves task instructions from the model.

        Precondition: task_name is an existing task
        Postcondition: Returns a string with how-to instructions for the task.
        """
        return self.maintenance_model.fetch_instructions(task_name)

    def update_task(
        self, task_name: str, notes: str, interval_days: int
    ) -> tuple[bool, str]:
        """
        Summary: Updates the reminder interval and or notes for a given task.

        Precondition:
            interval_days is a positive integer.
            task_name is an existing task

        Postcondition: Updates the interval in the model. Returns True if successful.
                        Also returns str with status message.
        """
        return self.maintenance_model.update_task(task_name, notes, interval_days)

    def create_task(
        self, task_name: str, notes: str, interval_days: int
    ) -> tuple[bool, str]:
        """
        Summary: Creates a maintenance task.

        Precondition: task_name is a non-existing task.
        Postcondition: Adds task to the database table. True if successful. Also returns str with status message
        """
        return self.maintenance_model.create_task(task_name, notes, interval_days)
