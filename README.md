# Task Manager

A simple command-line task manager written in Python. It runs interactively in
a terminal and allows you to:

- Add tasks with a custom title.
- View all tasks and their completion status.
- Mark tasks as complete.
- Delete tasks.
- Save tasks automatically between sessions.

Tasks are stored in `tasks.json`, so they remain available the next time you
run the app.

## Requirements

- Python 3.6 or later
- A terminal or command prompt

No third-party packages or dependencies are required.

## Project structure

| File                 | Purpose                                                                   |
| -------------------- | ------------------------------------------------------------------------- |
| `main.py`          | Starts the application and displays the interactive menu.                 |
| `manager.py`       | Loads, saves, adds, completes, and deletes tasks.                         |
| `task.py`          | Defines the `Task` class and task display format.                       |
| `tasks.json`       | Stores all saved tasks in JSON format.                                    |
| `requirements.txt` | Lists third-party Python dependencies (none currently).                   |
| `.gitignore`       | Excludes Python, virtual environment, and local task data files from Git. |
| `README.md`        | Contains setup and usage documentation.                                   |

## Setup and running

1. Install Python 3 and ensure `python` is available in your terminal.
2. Open a terminal.
3. Navigate to the application directory:

```powershell
cd app
```

4. Install the project dependencies:

```powershell
python -m pip install -r requirements.txt
```

The project currently has no third-party dependencies.

5. Start the application:

```powershell
python main.py
```

## Menu options

After startup, the application displays:

```text
Task Manager
1. Add Task
2. List Tasks
3. Complete Task
4. Delete Task
5. Exit
```

### 1. Add Task

Enter the task title when prompted. The task receives the next available ID,
is marked as pending, and is saved to `tasks.json`.

### 2. List Tasks

Displays every saved task in this format:

```text
Task 1: Learn Python - pending
Task 2: Build a project - Done
```

### 3. Complete Task

Enter the numeric ID of a task to mark it as done. The updated status is saved
to `tasks.json`.

### 4. Delete Task

Enter the numeric ID of a task to remove it. The remaining tasks are saved
after deletion.

### 5. Exit

Stops the application.

## Example workflow

To add a task, choose `1` and enter a title:

```text
Enter your choice: 1
Enter task title: Learn Python
Task 'Learn Python' added successfully.
```

Choose `2` to view tasks:

```text
Enter your choice: 2
Task 1: Learn Python - pending
```

To complete the task, choose `3` and enter its ID:

```text
Enter your choice: 3
Enter task ID to mark as done: 1
Task 1 marked as done.
```

The task now appears as complete:

```text
Enter your choice: 2
Task 1: Learn Python - Done
```

To close the application:

```text
Enter your choice: 5
Exiting...
```

## Task storage

Tasks are saved to `tasks.json` in the project directory. Each task includes an
ID, title, and completion status.

Example JSON entry:

```json
{
    "id": 1,
    "title": "Learn Python",
    "done": false
}
```

The application automatically creates or updates `tasks.json` when a task is
added, completed, or deleted.

## Important behavior

- Task IDs are numeric.
- Entering a task ID that does not exist displays an error message.
- Entering a non-numeric value at an ID prompt displays:
  `Invalid input. Please enter a valid number.`
- Keep `tasks.json` in the same directory as `main.py` and `manager.py`.
- Run the app from the project directory or another directory that provides
  access to `tasks.json`.

## Troubleshooting

### Python is not recognized

Verify that Python is installed and that its installation directory is in the
`PATH`. Open a new terminal and run:

```powershell
python --version
```

### `tasks.json` is missing

This is safe on the first run. The app starts with an empty task list and
creates or updates `tasks.json` when you add or modify a task.

### Invalid JSON

If `tasks.json` contains malformed JSON, the app may fail while loading it.
Restore valid JSON or replace the file with:

```json
[]
```
