from controllers.home_controller import HomeController
from flask import Flask, render_template

class HomeView:
    def __init__(self, controller: HomeController):
        """
        Summary: Initializes the HomeView with a reference to HomeController.

        Precondition: controller is an instance of HomeController.
        """
        self.controller = controller

    def display_navigation_options(self):
        """
        Summary: Displays navigation options for the user.
        Postcondition: User can choose to navigate to other views (may abstract part of html to here not sure yet)
        """
        pass 


    def display_home_screen(self):
        """
        Summary: Displays the home screen with greeting, bike info, recent tasks, and alerts.

        Postcondition: Shows all key home screen elements.
        """
        greeting = self.controller.get_greeting()
        bike_info = self.controller.get_bike_status_summary()
        recent_tasks = self.controller.get_recent_maintenance_tasks()
        overdue, upcoming = self.controller.get_upcoming_and_overdue_tasks()

        # Return rendered template directly
        return render_template("home.html",
                            greeting=greeting,
                            bike_info=bike_info,
                            recent_tasks=recent_tasks,
                            overdue=overdue,
                            upcoming=upcoming)
