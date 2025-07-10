from ..controllers.bike_controller import BikeController
class AddBikeView:
    def __init__(self, controller: BikeController):
        """
        Summary: Initializes the AddBikeView with a reference to the BikeController.

        Precondition: controller is an instance of BikeController.
        """
        self.controller = controller

    def display_form(self):
        """
        Summary: Displays the bike registration form to the user.

        Postcondition: Prompts user for bike details (type, brand, model, year, optional photo).
        """

    def display_success_message(self, message: str = "Bike registered successfully!"):
        """
        Summary: Shows a success message after successful submission.
        """
        print(message)

    def display_error_message(self, message: str):
        """
        Summary: Displays an error message if submission fails.

        Precondition: message is a non-empty string.
        """
        print(f"Error: {message}")

    def navigate_to_home(self):
        """
        Summary: Navigates to the HomeView.

        Postcondition: This would change the view. This will likely change I am unsure how this is going to work
        """
        print("Returning to home screen...")
