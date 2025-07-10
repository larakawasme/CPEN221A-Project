from ..controllers.home_controller import HomeController

class HomeView:
    def __init__(self, controller: HomeController):
        """
        Summary: Initializes the HomeView with a reference to HomeController.

        Precondition: controller is an instance of HomeController.
        """
        self.controller = controller

    def display_home_screen(self):
        """
        Summary: Displays the home screen with greeting, bike info, recent tasks, and alerts.

        Postcondition: Shows all key home screen elements.
        """
        # Depends on if bike exists or not
        pass

    def display_navigation_options(self):
        """
        Summary: Displays navigation options for the user.
        Postcondition: User can choose to navigate to other views (not sure how to show this)
        """
        pass 