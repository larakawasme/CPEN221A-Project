from database import get_db
from datetime import datetime


class ChecklistModel:
    def __init__(self):
        """
        Summary: Initializes the ChecklistModel and connects to the SQLite database.
        """
        # Initialize database connection here (placeholder)
        pass

    def get_checklist_tasks(self) -> list[dict]:
        """
        Summary: Retrieves all current checklist items (default and custom).

        Postcondition: Returns a list of item dictionaries.
        """
        con = get_db()
        cursor = con.cursor()
        cursor.execute(
            """
            SELECT checklist_tasks.id, maintenance_tasks.id, maintenance_tasks.task_name
            FROM checklist_tasks
            JOIN maintenance_tasks ON checklist_tasks.maintenance_id = maintenance_tasks.id
            """
        )
        rows = cursor.fetchall()
        cursor.close()
        tasks = []

        for row in rows:
            tasks.append(
                {
                    "checklist_task_id": row[0],
                    "maintenance_id": row[1],
                    "task_name": row[2],
                }
            )

        return tasks

    def start_new_checklist_session(self) -> None:
        """
        Summary: Clears the current checklist_session table and inserts all checklist tasks as uncompleted.

        Precondition: checklist has tasks
        Postcondition: checklist_session table is ready and all tasks are marked as uncompleted
        """
        con = get_db()
        cursor = con.cursor()

        cursor.execute("DELETE FROM checklist_session")  # Clear old table

        # Insert all checklist tasks into the session as uncompleted
        cursor.execute("SELECT id FROM checklist_tasks")
        checklist_task_ids = cursor.fetchall()

        for row in checklist_task_ids:
            checklist_task_id = row["id"]
            cursor.execute(
                "INSERT INTO checklist_session (checklist_task_id, completed) VALUES (?, 0)",
                (checklist_task_id,),
            )

        con.commit()
        cursor.close()

    def mark_task_completed(self, checklist_task_id: int) -> tuple[bool, str]:
        """
        Summary: Marks a checklist task as completed and records the timestamp of checklist completion in mainteance_tasks table

        Precondition: checklist_session has tasks in it.
        Postcondition: task is marked as completed in session and maintenace_tasks table is up to date with last completed date.
                        Returns True if successful. Returns status message.
        """
        try:
            con = get_db()
            cursor = con.cursor()

            # Mark task as completed
            cursor.execute(
                "UPDATE checklist_session SET completed = 1 WHERE checklist_task_id = ?",
                (checklist_task_id,),
            )
            # Get ID
            cursor.execute(
                "SELECT maintenance_id FROM checklist_tasks WHERE id = ?",
                (checklist_task_id,),
            )
            maintenance_row = cursor.fetchone()
            if not maintenance_row:
                return False, "Error: Checklist task not found in maintenance tasks."

            maintenance_id = maintenance_row["maintenance_id"]

            # Update maintenance task last_completed to now
            current_time = datetime.now().isoformat()
            cursor.execute(
                "UPDATE maintenance_tasks SET last_completed = ? WHERE id = ?",
                (current_time, maintenance_id),
            )

            con.commit()
            task_row = cursor.fetchone()
            cursor.close()

            task_name = task_row["task_name"]
            return True, f"{task_name} completed"
        except Exception as e:
            return False, f"Error marking task completed: {e}"

    def customize_checklist(self, items: list[dict]) -> tuple[bool, str]:
        """
        Summary: Updates the checklist by adding and/or removing items.

        Precondition:
            items is a list of dictionaries, each with keys:
                'task_name': the name of the checklist item
                'action': either 'add' or 'remove'

        Postcondition: Updates stored checklist items. Returns True if successful along with status message.
        """
        try:
            con = get_db()
            cursor = con.cursor()

            for item in items:
                task_name = item.get("task_name")
                action = item.get("action")

                if action == "add":
                    interval = item.get("interval")
                    # Check if maintenance task exists
                    cursor.execute(
                        "SELECT id FROM maintenance_tasks WHERE task_name = ?",
                        (task_name,),
                    )
                    row = cursor.fetchone()
                    if row:
                        maintenance_id = row[0]
                    else:
                        # If doesn't exist, add it with interval_days if provided
                        if interval is not None:
                            cursor.execute(
                                "INSERT INTO maintenance_tasks (task_name, interval_days) VALUES (?, ?)",
                                (task_name, interval),
                            )
                        else:
                            cursor.execute(
                                "INSERT INTO maintenance_tasks (task_name) VALUES (?)",
                                (task_name,),
                            )
                        cursor.execute(
                            "SELECT id FROM maintenance_tasks WHERE task_name = ?",
                            (task_name,),
                        )
                        row = cursor.fetchone()
                        maintenance_id = row[0]
                    # Add to checklist_tasks
                    cursor.execute(
                        "INSERT INTO checklist_tasks (maintenance_id) VALUES (?)",
                        (maintenance_id,),
                    )
                else:  # remove
                    cursor.execute(
                        "SELECT id FROM maintenance_tasks WHERE task_name = ?",
                        (task_name,),
                    )
                    row = cursor.fetchone()
                    if row:
                        maintenance_id = row[0]
                        cursor.execute(
                            "DELETE FROM checklist_tasks WHERE maintenance_id = ?",
                            (maintenance_id,),
                        )
            con.commit()
            cursor.close()
            return True, "Checklist updated successfully."
        except Exception as e:
            return False, f"Error customizing checklist: {e}"
