from ..controllers.maintenance_controller import MaintenanceController

class MaintenanceHistoryView:
    def __init__(self, controller: MaintenanceController):
        """
        Summary: Initializes the MaintenanceHistoryView with a reference to MaintenanceController.

        Precondition: controller is an instance of MaintenanceController.
        """
        self.controller = controller

    def display_maintenance_history(self):
        """
        Summary: Displays maintenance history including task names, last completed dates, notes,
        and alerts for overdue and upcoming tasks.

        Postcondition: Outputs the maintenance task history and alerts section.
        """
        pass

    def mark_task_completed(self, task_name: str):
        """
        Summary: Prompts user to confirm completion of a maintenance task and optional notes,
        then submits this info to the controller.

        Precondition: task_name is the name of an existing maintenance task.

        Postcondition: Sends completion data to controller. Displays success or error message.
        """
        pass

    def view_task_instructions(self, task_name: str):
        """
        Summary: Fetches and displays how-to instructions for a maintenance task.

        Precondition: task_name is the name of an existing maintenance task.

        Postcondition: Outputs instructions to the user.
        """
        pass

    def edit_reminder_interval(self, task_name: str):
        """
        Summary: Allows the user to update the reminder interval (in days) for a maintenance task.

        Precondition: task_name is the name of an existing maintenance task.

        Postcondition: Sends new interval to controller and displays success/error.
        """
        pass

    def display_success_message(self, message: str = "Operation completed successfully."):
        """
        Summary: Displays a success message.

        Precondition: message is a non-empty string.
        """
        print(message)

    def display_error_message(self, message: str):
        """
        Summary: Displays an error message.

        Precondition: message is a non-empty string.
        """
        print(f"Error: {message}")

    def navigate_to_home(self):
        """
        Summary: Navigates back to the HomeView.

        Postcondition: This would change the view. This will likely change I am unsure how this is going to work
        """
        print("Returning to home screen...")
