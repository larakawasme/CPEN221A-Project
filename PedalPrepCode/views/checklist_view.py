from controllers.checklist_controller import ChecklistController
from flask import request, render_template, redirect, url_for


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
        if request.method == "POST":
            completed_items = request.form.getlist("completed")
            all_items = [
                item["task_name"] for item in self.controller.get_checklist_items()
            ]

            if len(completed_items) < len(all_items):
                # Show warning before proceeding
                if not request.form.get("confirm_skip"):
                    return render_template(
                        "checklist.html",
                        items=self.controller.get_checklist_items(),
                        warning="You skipped a safety step. Are you sure you want to continue?",
                        completed_items=completed_items,
                    )

            self.controller.submit_checklist_completion(completed_items=completed_items)
            return redirect(url_for("home"))

        # GET request — just show the checklist
        return render_template(
            "checklist.html", items=self.controller.get_checklist_items()
        )

    def customize_checklist(self):
        """
        Summary: Allows the user to add or remove checklist items.

        Postcondition: Updates checklist through the controller.
        """
        maintenance_tasks = self.controller.maintenance_model.get_tasks()
        if request.method == "POST":
            action = request.form.get("action")
            new_task = request.form.get("new_task")
            interval = request.form.get("interval")
            existing_task = request.form.get("existing_task")
            items = self.controller.get_checklist_items()

            if action == "remove":
                task_name = request.form.get("task_name")
                self.controller.update_checklist_customization(task_name, "remove")
            elif action == "add":
                # Prefer existing task if selected
                task_name = existing_task if existing_task else new_task
                if task_name:
                    item = {"task_name": task_name, "action": "add"}
                    if interval:
                        item["interval"] = int(interval)
                    self.controller.update_checklist_customization(
                        item["task_name"], item["action"], interval=item.get("interval")
                    )

            # Refresh items after update
            items = self.controller.get_checklist_items()
        else:
            items = self.controller.get_checklist_items()

        return render_template(
            "edit_checklist.html", items=items, maintenance_tasks=maintenance_tasks
        )
