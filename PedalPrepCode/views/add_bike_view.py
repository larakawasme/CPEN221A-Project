from controllers.bike_controller import BikeController
from flask import request, render_template


class AddBikeView:
    def __init__(self, controller: BikeController):
        """
        Summary: Initializes the AddBikeView with a reference to the BikeController.

        Precondition: controller is an instance of BikeController.
        """
        self.controller = controller

    def display_bike_registration_form(self):
        """
        Summary: Displays the bike registration form to the user.

        Postcondition: Prompts user for bike details (type, brand, model, year, optional photo).
        """
        message = None
        message_type = "success"
        redirect_after = False

        if request.method == "POST":
            bike_type = request.form.get("type")
            brand = request.form.get("brand")
            model = request.form.get("model", "")
            year = request.form.get("year", "")

            success, message = self.controller.handle_bike_submission(
                bike_type, brand, model, year
            )

            message_type = "success" if success else "danger"
            redirect_after = True if success else False

        return render_template(
            "add_bike.html",
            message=message,
            message_type=message_type,
            redirect_after=redirect_after,
        )

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
