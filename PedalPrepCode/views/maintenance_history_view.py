from controllers.maintenance_controller import MaintenanceController
from flask import request, render_template, redirect, url_for


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
        message = None
        message_type = "success"

        if request.method == "POST":
            action = request.form.get("action")
            task_name = request.form.get("task_name")

            if action == "complete" and task_name:
                notes = request.form.get("notes", "")
                success, message = self.controller.mark_task_completed(task_name, notes)
                message_type = "success" if success else "danger"

        # GET request
        tasks = self.controller.get_task_history()
        overdue, upcoming = self.controller.get_upcoming_and_overdue_tasks()
        return render_template(
            "maintenance_history.html",
            tasks=tasks,
            overdue=overdue,
            upcoming=upcoming,
            message=message,
            message_type=message_type,
        )

    def display_edit_maintenance_tasks(self):
        mode = request.args.get("mode", "edit")  # Default to edit

        if request.method == "POST":
            task_name = request.form.get("task_name")
            notes = request.form.get("notes") or None
            interval_days = request.form.get("interval_days")
            interval_days = int(interval_days) if interval_days else None

            if mode == "edit":
                success, message = self.controller.update_task(
                    task_name, notes, interval_days
                )
            elif mode == "add":
                success, message = self.controller.create_task(
                    task_name, notes, interval_days
                )
            else:
                return render_template(
                    "edit_maintenance.html",
                    message="Invalid mode.",
                    message_type="danger",
                )

            message_type = "success" if success else "danger"

            return render_template(
                "edit_maintenance.html", message=message, message_type=message_type
            )

        tasks = self.controller.get_task_history()
        return render_template("edit_maintenance.html", tasks=tasks, mode=mode)

    def navigate_to_home(self):
        """
        Summary: Navigates back to the HomeView.

        Postcondition: This would change the view. This will likely change I am unsure how this is going to work
        """
        print("Returning to home screen...")
