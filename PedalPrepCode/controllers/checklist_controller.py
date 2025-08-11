from models.checklist_model import ChecklistModel
from models.maintenance_model import MaintenanceModel


class ChecklistController:
    def __init__(
        self, checklist_model: ChecklistModel, maintenance_model: MaintenanceModel
    ):
        """
        Summary: Initializes the controller with references to ChecklistModel and MaintenanceModel.

        Precondition: checklist_model is an instance of ChecklistModel.
                      maintenance_model is an instance of MaintenanceModel.
        """
        self.checklist_model = checklist_model
        self.maintenance_model = maintenance_model

    def get_checklist_items(self) -> list[dict]:
        """
        Summary: Retrieves current checklist items (default and custom).
        Postcondition: Returns a list of checklist items.
        """
        return self.checklist_model.get_items()

    def submit_checklist_completion(
        self, completed_items: list[str], allow_incomplete: bool
    ) -> bool:
        """
        Summary: Submits checklist completion and updates timestamps.

        Precondition:
            completed_items is a list of item names.
            allow_incomplete is True if user confirmed skipping items.

        Postcondition:
            Records timestamp of checklist completion.
            Updates maintenance model for relevant items.
            Returns True if successfully recorded.
        """
        return self.checklist_model.record_completion()

    def update_checklist_customization(
        self, new_items: list[dict], removed_items: list[dict]
    ) -> bool:
        """
        Summary: Customizes the checklist by adding/removing items.

        Precondition:
            new_items and removed_items are lists of dicts that contain item names and option how to complete

        Postcondition: ChecklistModel is updated accordingly. Returns True if successful.
        """
        return self.checklist_model.customize_checklist(
            new_items=new_items, removed_items=removed_items
        )

    def warn_for_incomplete(self, completed_items: list[str]) -> bool:
        """
        Summary: Determines whether a warning should be shown for incomplete checklist.
        Called by ChecklistView

        Precondition: completed_items is a list of checked item names.

        Postcondition: Returns True if there are unchecked required items.
        """
        return True
