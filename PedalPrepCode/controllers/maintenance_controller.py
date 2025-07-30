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
        return self.maintenance_model.get_recent_tasks()

    def get_upcoming_and_overdue_tasks(self) -> tuple[list[dict], list[dict]]:
        """
        Summary: Determines which tasks are upcoming and which are overdue.

        Postcondition: Returns two lists of task dictionaries: (overdue_tasks, upcoming_tasks)
        """
        upcoming, overdue = self.maintenance_model.get_upcoming_and_overdue_tasks()
        # maybe some more cleaning logic
        return upcoming, overdue
    
    def mark_task_completed(self, task_name: str, notes: str = "") -> bool:
        """
        Summary: Marks a maintenance task as completed.

        Precondition: task_name is an existing task
        Postcondition: Updates model with current timestamp and optional notes. Returns True if successful.
        """
        return self.maintenance_model.complete_task(task_name, notes)

    def get_task_instructions(self, task_name: str) -> str:
        """
        Retrieves task instructions from the model.
        
        Precondition: task_name is an existing task
        Postcondition: Returns a string with how-to instructions for the task.
        """
        return self.maintenance_model.fetch_instructions(task_name)

    def update_task_interval(self, task_name: str, days: int) -> bool:
        """
        Updates the reminder interval for a given task.

        Precondition: 
            days is a positive integer.
            task_name is an existing task

        Postcondition: Updates the interval in the model. Returns True if successful.
        """
        return self.maintenance_model.set_task_interval(task_name, days)
