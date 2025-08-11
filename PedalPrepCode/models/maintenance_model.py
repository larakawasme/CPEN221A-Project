from database import get_db
from datetime import datetime, timedelta


class MaintenanceModel:
    def __init__(self):
        """
        Summary: Initializes the MaintenanceModel and connects to the SQLite database.
        """
        pass

    def get_tasks(self) -> list[dict]:
        """
        Summary: Retrieves maintenance tasks history.

        Postcondition: Returns a list of dictionaries with keys: 'task_name', 'last_completed', 'notes'.
        """
        try:
            con = get_db()
            cursor = con.cursor()
            cursor.execute(
                "SELECT task_name, last_completed, notes, interval_days FROM maintenance_tasks"
            )
            rows = cursor.fetchall()
            cursor.close()
            tasks = []
            for row in rows:
                tasks.append(
                    {
                        "task_name": row[0],
                        "last_completed": row[1],
                        "notes": row[2],
                        "interval_days": row[3],
                    }
                )
            return tasks

        except Exception as e:
            # Should handle this more elegantly in the future, leaving as so for now
            message = f"Error occured while trying to fetch maintenace information: {e}"
            raise Exception

    def complete_task(self, task_name: str, notes: str = "") -> tuple[bool, str]:
        """
        Summary: Marks a maintenance task as completed with the current timestamp and optional notes.

        Precondition: task_name is an existing task.
        Postcondition: Updates task completion record and returns True if successful.
                        Also returns str with status message.
        """
        try:
            con = get_db()
            cursor = con.cursor()
            current_date_time = datetime.now().isoformat()

            # Insert new task if none exists, else update last_completed and notes
            cursor.execute(
                """
                INSERT INTO maintenance_tasks (task_name, last_completed, notes)
                VALUES (?, ?, ?)
                ON CONFLICT(task_name) DO UPDATE SET
                  last_completed=excluded.last_completed,
                  notes=excluded.notes
            """,
                (task_name, current_date_time, notes),
            )
            con.commit()
            cursor.close()
            return True, f"Task '{task_name}' marked as completed."

        except Exception as e:
            return (
                False,
                f"Error occured while trying to update maintenace information for task '{task_name}: {e}",
            )

    def create_task(
        self, task_name: str, notes: str = "", interval_days: int = 30
    ) -> tuple[bool, str]:
        """
        Summary: Creates a maintenance task.

        Precondition: task_name is a non-existing task.
        Postcondition: Adds task to the database table. True if successful. Also returns str with status message
        """
        try:
            con = get_db()
            cursor = con.cursor()
            cursor.execute(
                """
                INSERT INTO maintenance_tasks (task_name, notes, interval_days)
                VALUES (?, ?, ?)
            """,
                (task_name, notes, interval_days),
            )
            con.commit()
            cursor.close()
            return True, f"Task '{task_name}' added."

        except Exception as e:
            return False, f"Failed to add task '{task_name}': {e}"

    def fetch_instructions(self, task_name: str) -> str:
        """
        Summary: Retrieves how-to instructions for the specified maintenance task.

        Precondition: task_name is an existing task.

        Postcondition: Returns a string with instructions.
        """
        return "Instructions for task."

    def update_task(
        self, task_name: str, notes: str = None, interval_days: int = None
    ) -> tuple[bool, str]:
        """
        Summary: Sets or updates the reminder interval (in days) and/or notes for a maintenance task.

        Precondition: days is a positive integer.
                      task_name is an existing task.

        Postcondition: Updates the task interval and/or notes and returns True if successful.
                        Also returns str with status message.
        """
        try:
            con = get_db()
            cursor = con.cursor()

            updates = []
            params = []

            if notes is not None:
                updates.append("notes = ?")
                params.append(notes)
            if interval_days is not None:
                updates.append("interval_days = ?")
                params.append(interval_days)

            if not updates:
                return False, "No fields to update."

            params.append(task_name)

            cursor.execute(
                f"""
                UPDATE maintenance_tasks
                SET {", ".join(updates)}
                WHERE task_name = ?
            """,
                tuple(params),
            )
            con.commit()
            cursor.close()

            return True, f"Task '{task_name}' updated."
        except Exception as e:
            return False, f"Failed to update task '{task_name}': {e}"

    def set_task_interval(self, task_name: str, days: int) -> tuple[bool, str]:
        """
        Summary: Sets or updates the reminder interval (in days) for a maintenance task.

        Precondition: days is a positive integer.
                      task_name is an existing task.

        Postcondition: Updates the task interval and returns True if successful.
                        Also returns str with status message.
        """
        try:
            con = get_db()
            cursor = con.cursor()
            cursor.execute(
                "UPDATE maintenance_tasks SET interval_days=? WHERE task_name=?",
                (days, task_name),
            )

            con.commit()
            cursor.close()
            return True, f"Reminder interval for '{task_name}' updated."

        except Exception as e:
            return False, f"Failed to update reminder interval for '{task_name}' : {e}."

    def get_upcoming_and_overdue_tasks(self) -> tuple[list[dict], list[dict]]:
        """
        Summary: Retrieves upcoming and overdue maintenance tasks based on schedule and completion dates.

        Postcondition: Returns a tuple: (overdue_tasks, upcoming_tasks), each a list of task dictionaries.
        """
        tasks = self.get_tasks()
        upcoming = []
        overdue = []
        current_date_time = datetime.now()

        for task in tasks:
            last_completed_str = task["last_completed"]
            interval = task.get("interval_days", 30)
            if last_completed_str:
                last_date = datetime.fromisoformat(last_completed_str)
                due_date = last_date + timedelta(days=interval)
                days_until_due = (due_date - current_date_time).days
                if days_until_due < 0:
                    overdue.append(task)
                elif days_until_due <= 7:  # Upcoming within a week
                    upcoming.append(task)
            else:
                # Never completed task considered overdue
                overdue.append(task)
        return overdue, upcoming
