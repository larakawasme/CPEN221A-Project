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
        Summary: Retrieves current checklist items (default and custom). Just a wrapped.
        Postcondition: Returns a list of checklist items.
        """
        return self.checklist_model.get_checklist_tasks()

    def submit_checklist_completion(self, completed_items: list[str]) -> bool:
        """
        Summary: Submits checklist completion and updates timestamps.

        Precondition:
            completed_items is a list of task names.

        Postcondition:
            Records timestamp of checklist completion.
            Updates maintenance model for relevant items.
            Returns True if successfully recorded.
        """
        all_tasks = self.checklist_model.get_checklist_tasks()
        # Map tasks to ID to mark as completed
        name_to_id = {
            task["task_name"]: task["checklist_task_id"] for task in all_tasks
        }
        for name in completed_items:
            checklist_task_id = name_to_id.get(name)
            if checklist_task_id:
                success, _ = self.checklist_model.mark_task_completed(checklist_task_id)
                if not success:
                    return False
        return True

    def update_checklist_customization(
        self, task_name: str, action: str, interval: int = None
    ) -> bool:
        """
        Summary: Customizes the checklist by adding or removing a single item.

        Precondition:
            task_name is the name of the checklist item.
            action is either 'add' or 'remove'.

        Postcondition: ChecklistModel is updated accordingly. Returns True if successful.
        """
        item = {"task_name": task_name, "action": action}
        if interval is not None and action == "add":
            item["interval"] = interval
        return self.checklist_model.customize_checklist([item])
