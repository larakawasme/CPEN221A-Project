# Requirements
I outline the requirements based on each of the application’s pages

## Home screen page
- Homescreen should greet user with a message (e.g. “Good morning”, “Welcome back”)
- If no bike is registered yet, the home screen has a button to “Add a bike” and takes you to the Add Bike page
- If a bike exists
    - The home screen displays  a section labeled“Bike status summary” 
        - The home screen must show up to 3 most recently completed maintenance tasks.
        - If fewer than 3 tasks have been completed, the section must display only the available items or remain blank.
    - The home screen will display alerts for upcoming or overdue tasks
        - Will show overdue items in red
        - Will show upcoming tasks in a neutral colour: grey or soft green
    - The home screen will have two quick action buttons
        - “Pre-ride checklist”: which will take you to pre ride checklist pae
        - “Maintenance history”: which will take you to Maintenance history page

## Pre-ride checklist page
- There is a button on the home page that navigates to this page
- Should have a “Back to homepage” button 
- This page should display a list of items, each with a checkbox for the user to check off. Also contains a “complete” button to - - confirm done with checklist
- Once the checklist is completed
    - System records the timestamp of completion
    - The system should update relevant last-completed maintenance data
    - The user should be redirected to the home page
- If user attempts to finish the checklist without checking all the items
    - The system will show a warning: “You skipped a safety step. Are you sure you want to continue?” Then will allow user to go back or proceed
- The checklist should be customizable
    - To customize the checklist, there will be a button called “Edit” or “Modify”
    - Users can select which items appear
    - Users can add items to the default
- The default checklist should have
    - Test brakes
    - Inspect chain for dryness
    - Check shifting is smooth
    - Check tire pressure

## Maintenance history page
- There is a button on the home page that navigates to this page
- Should have “Back to homepage” button
- Should display summary of all maintenance tasks
    - Each task must include: task name, date last completed, and optional user-entered notes
- Maintenance reminders will be based on time intervals
- Page will display alerts of overdue and upcoming tasks
    - Overdue tasks will be shown in red
    - Upcoming tasks will be shown in a neutral colour: grey or soft green
    -Schedule of tasks is based on elapsed time since last time of completion.These will be written into the system but users can modify this
- Users should be able to mark tasks as completed
    - When a user marks tasks as completed, it will update the last completed date and offer option to update the notes
- App will provide basic instructions on how to complete the task

## Add Bike page
- There is a button on the home page that navigates to this page
- User must enter
    - Type of bike (selected from dropdown of “Road”, “Commuter”)
    - Brand (text input)
    - Model (optional text input)
- The “Add Bike” form won’t submit unless the required fields are done
    - If form incomplete, app will show an error “Please completed bike information”
- Upon successful bike entry, user is returned to home page

### General system requirements
- The system must store
    - The bike’s details (MVP will support one bike)
    - Maintenance task history (task name, date, notes)
    - Pre-ride checklist
- Only maintenance history from past a certain time period (TBD, implementation dependent) must be shown. Rest will be discarded
