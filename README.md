# Task Tracker CLI

A simple command line task tracker built with Python. It allows users to manage their daily tasks directly from the terminal.

## Features

- Add new tasks.
- List all tasks.
- List tasks by status.
- Update task descriptions.
- Delete tasks.
- Mark tasks as in-progress or done.
- Store tasks in a JSON file.
- Automatically generate task IDs.
- Track task creation and update dates.

## Requirements

- Python 3 installed.
- Git (optional, for cloning the repository).

## Installation

1. Clone the repository:

   ```bash
   git clone YOUR_REPOSITORY_URL
   ```

2. Navigate into the project directory:

   ```bash
   cd Task-Tracker
   ```

3. Run the application:

   ```bash
   python taskManager.py
   ```

## Usage

### Add a task

```bash
python taskManager.py add "Learn Python"
```

### List all tasks

```bash
python taskManager.py list
```

### List tasks by status

```bash
python taskManager.py list todo
python taskManager.py list in-progress
python taskManager.py list done
```

### Update a task

```bash
python taskManager.py update 1 "Learn C#"
```

### Delete a task

```bash
python taskManager.py delete 1
```

### Mark a task as in-progress

```bash
python taskManager.py mark-in-progress 1
```

### Mark a task as done

```bash
python taskManager.py mark-done 1
```

## Technologies Used

- Python
- JSON
- Git and GitHub

## Data Storage

Tasks are stored locally in a JSON file named `todo.json`. The file is created automatically when it does not exist.

~Suzy.404
