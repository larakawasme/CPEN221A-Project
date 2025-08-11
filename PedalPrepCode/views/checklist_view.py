from ..controllers.checklist_controller import ChecklistController


class ChecklistView:
    def __init__(self, controller: ChecklistController):
        """
        Summary: Initializes the ChecklistView with a reference to ChecklistController.

        Precondition: controller is an instance of ChecklistController.
        """
        self.controller = controller

    def display_checklist(self):
        """
        Summary: Displays the checklist items and allows user to mark them as completed.

        Postcondition: Prompts user to check off items and handles completion submission.
        """
        pass

    def display_completion_message(self):
        """
        Summary: Shows success message after submitting checklist.
        """
        print("Checklist completed and saved.")

    def display_error_message(self, message: str):
        """
        Summary: Displays an error message.

        Precondition: message is a non-empty string.
        """
        print(f"Error: {message}")

    def customize_checklist(self):
        """
        Summary: Allows the user to add or remove checklist items.

        Postcondition: Updates checklist through the controller.
        """
        pass

    def navigate_to_home(self):
        """
        Summary: Navigates back to the HomeView.
        Postcondition: This would change the view. This will likely change I am unsure how this is going to work
        """
        print("Returning to home screen...")
