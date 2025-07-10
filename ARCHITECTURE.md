# Pedal Prep – Architecture Description

This document describes all major components (models, controllers, and views) of the Pedal Prep application, their responsibilities, where they reside, and how they communicate.

---
## Models

### `BikeModel`

**Responsibility:**  
  Stores details about the user’s bike including type, brand, and model.

**Resides:**  
  Server only (data stored in SQLite database).

**Communication and abilities:**  
  Communicates with `BikeController` (client).  
  The `BikeController` sends requests to `BikeModel` to:
  - Create or update bike information.
  - Retrieve bike details for display.

---

### `MaintenanceModel`

**Responsibility:**  
- Stores maintenance tasks history, including task names, completion dates, and optional notes.
- Stores and updates user-defined schedule intervals for each tasks.
- Filters history retrieval to only include records within allowed time window (TBD). Older records are deleted.

**Resides:**  
  Server only (data stored in SQLite database).

**Communication:**  
  Communicates with `MaintenanceController` (client).  
  The `MaintenanceController` sends requests to `MaintenanceModel` to:
  - Retrieve maintenance history.
  - Mark tasks as completed and update notes.
	- Each time a task is completed, a new item is added in the model with the completion data and notes.
  - Get maintenance task instructions.


### ChecklistModel

**Responsibility:**  
  Stores the pre-ride checklist items (default and customized) and timestamps of checklist completions.

**Resides:**  
  Server only (data stored in SQLite database).

**Communication:**  
  Communicates with `ChecklistController` (client).  
  The `ChecklistController` sends requests to `ChecklistModel` to:
  - Retrieve current checklist items.
  - Update checklist customization.
  - Record checklist completion timestamps.
---
## Controllers

### HomeController

**Responsibility:**  
Handles data retrieval for the `HomeView`, including greeting message, bike summary, recent maintenance tasks, and alerts. 

**Resides:**  
  Server side.

**Communication:**  
  Communicates with:
  - `BikeModel`  to fetch bike data.
  - `MaintenanceModel` to fetch recent maintenance tasks and alerts (upcoming and overdue tasks).

### BikeController

**Responsibility:**  
  Manages bike registration and updates from the user input on the `AddBikeView`. 

**Resides:**  
  Server side.

**Communication:**  
  Communicates with `BikeModel` to:
  - Send new or updated bike information.
  - Receive confirmation or error responses.
Validates user input and blocks submission if required fields (type, brand) are missing. Returns error message to the view.


### MaintenanceController

**Responsibility:**  
- Manages user interactions on the `MaintenanceHistoryView` including displaying maintenance task summaries, handling task completion actions, updating notes, and retrieving maintenance instructions.
- Determines which tasks are upcoming and overdue.
- Filters task history by date.
- Format tasks with color/warning flags for views.
- Handles user input to modify pre-existing task reminder intervals .

**Resides:**  
  Server side.

**Communication:**  
  Communicates with `MaintenanceModel` to:
  - Fetch maintenance task history.
  - Updates completed tasks with completion time and notes.
  - Retrieve task instructions when expanding a task to complete.

### ChecklistController

**Responsibility:**  
  Manages the pre-ride `ChecklistView`, including displaying checklist items, recording completion, handling warnings for incomplete steps, and customizing checklist content.

**Resides:**  
Server side

**Communication:**  
  Communicates with `ChecklistModel`  to:
  - Get checklist items.
  - Submit checklist completion.
  - Update customized checklist items.
Communicates with `MaintenanceModel` to update last completed dates for tasks completed in checklist completion.
- If not all checklist items are checked, shows warning dialog and gives user option to proceed or return.

---

## Views

### HomeView

**Responsibility:**  
  Displays greeting, bike status summary, upcoming and overdue tasks, and navigation buttons. It is the homepage

**Resides:**  
  Client only.

**Communication:**  
  Receives data and commands from `HomeController`.

**UI Elements:**
  - Greeting message (e.g., "Good morning", "Welcome back")
  - If no bike exists:  
    - **"Add a Bike"** button navigates to `AddBikeView`
  - If bike exists:
    - **"Bike Status Summary"** section
    - List: Up to 3 most recently completed maintenance tasks
    - **"Alerts"** section:
      - Overdue tasks shown in red
      - Upcoming tasks shown in grey or soft green
  - Quick Action Buttons:
    - **"Pre-Ride Checklist"** navigates to `ChecklistView`
    - **"Maintenance History"** navigates to `MaintenanceHistoryView`

### AddBikeView

**Responsibility:**  
  Displays the bike registration form for user input and submission.

**Resides:**  
  Client only.

**Communication:**  
  Interacts with `BikeController` for form submission and validation feedback.

**UI Elements:**
  - Form:
    - Dropdown: **Bike Type** (e.g., Road, Commuter) – *required*
    - Text input: **Brand** – *required*
    - Text input: **Model** – *optional*
    -Option to upload photo and will process information from image

  - **"Submit"** Button: 
    - If valid:
        - Saves bike info and redirects to `HomeView`
    - If incomplete:
 	    - Displays error: **"Please complete bike information."**
  - **"Back to Homepage"** button navigates `HomeView`

---

### ChecklistView

**Responsibility:**  
  Shows the checklist items with checkboxes, allows users to mark items complete, customize the list, and submit completion.

**Resides:**  
  Client only.

**Communication:**  
  Interacts with `ChecklistController` to get data and send updates.

**UI Elements:**
  - **"Pre-Ride Checklist"** section
  - Checklist items with checkboxes:
    - Default items:
      - Test brakes
      - Inspect chain for dryness
      - Check shifting is smooth
      - Check tire pressure
    - Any custom user-added items
  - **"Complete Checklist"** button
    - If all items checked: records timestamp and redirects to home
    - If not all checked: 
        - shows warning:  
            - "You skipped a safety step. Are you sure you want to continue?"  
        - Options: **Go back** or **Proceed anyway** buttons
  - **"Edit Checklist"** button allows you to edit and add tasks to checklist
  - **"Back to Homepage"** button navigates `HomeView`

---

### MaintenanceHistoryView

**Responsibility:**  
  Displays all maintenance tasks with name, last completion date, optional notes, and overdue/upcoming alerts.

**Resides:**  
  Client only.

**Communication:**  
  Interacts with `MaintenanceController` for data retrieval and updates.

- **Communicates with:**  
  `MaintenanceController`

- **UI Elements:**
  - **"Summary"** section
  - List of maintenance tasks:
    - Task name
    - Last completed date
    - Notes (if any)
- **"Alerts"** section
      - Overdue tasks in red
      - Upcoming tasks in grey or soft green
    -  Can mark items as completed by selecting **"Mark as Completed"**  next to item
      	- Opens dialog to confirm completion and add notes  
      	- Sends updated info to `Maintenancecontroller`
    - Can select  **"View Instructions"**  to see how to complete the task
      - Expands task to show how-to steps
  - **"Back to Homepage"** button navigates to `HomeView`
  - Section to edit reminder intervals

