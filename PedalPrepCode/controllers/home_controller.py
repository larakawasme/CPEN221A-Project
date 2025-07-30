from models.maintenance_model import MaintenanceModel
from models.bike_model import BikeModel
class HomeController:
    def __init__(self, bike_model: BikeModel, maintenance_model: MaintenanceModel):
        """
        Summary: Initializes the controller with references to BikeModel and MaintenanceModel.

        Precondition: bike_model is an instance of BikeModel.
                      maintenance_model is an instance of MaintenanceModel.
        """
        self.bike_model = bike_model
        self.maintenance_model = maintenance_model

    def get_greeting(self) -> str:
        """
        Summary: Generates a greeting message based on time of day.

        Called by: HomeView

        Postcondition: Returns a string greeting (e.g., "Good morning", "Welcome back").
        """
        return "Welcome back!"

    def get_bike_status_summary(self) -> dict:
        """
        Summary: Retrieves summary details of the registered bike.

        Called by: HomeView

        Postcondition: Returns bike info dict or None if no bike registered.
        """
        return self.bike_model.get_bike_info()

    def get_recent_maintenance_tasks(self, max_tasks: int = 3) -> list[dict]:
        """
        Summary: Retrieves up to max_tasks most recently completed maintenance tasks.

        Called by: HomeView

        Postcondition: Returns a list of maintenance task dictionaries.
        """
        all_tasks = self.maintenance_model.get_recent_tasks()
        return all_tasks[:max_tasks]

    def get_upcoming_and_overdue_tasks(self) -> tuple[list[dict], list[dict]]:
        """
        Summary: Retrieves upcoming and overdue maintenance tasks with alert info.

        Called by: HomeView

        Postcondition: Returns a List of 'overdue' and 'upcoming' task dicts.
        """
        overdue, upcoming = self.maintenance_model.get_upcoming_and_overdue_tasks()
        return overdue, upcoming
