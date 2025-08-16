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
        # Accept message from query string for banner
        message = request.args.get("message")
        message_type = request.args.get("message_type", "success")

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

    def add_to_checklist(self):
        """
        Summary: Adds a maintenance task to the checklist from the maintenance history page.

        Postcondition: The specified task is added to the checklist (if not already present),
                        and the user is redirected back to the maintenance history page with a success message.
        """
        task_name = request.form.get("task_name")
        message = None
        message_type = "success"
        if task_name:
            self.controller.update_checklist_customization(task_name, "add")
            message = f"'{task_name}' added to checklist."
        return redirect(
            url_for("maintenance_history", message=message, message_type=message_type)
        )
