import json
import sys
from datetime import datetime

FILE = "todo.json"

try:
    with open(FILE, "r") as file:
        tasks = json.load(file)

except FileNotFoundError:
    tasks = []

    with open(FILE, "w") as file:
        json.dump(tasks, file, indent=4)


def save_tasks():
    with open(FILE, "w") as file:
        json.dump(tasks, file, indent=4)


def add_task(description):
    task = {
        "id": max([t["id"] for t in tasks], default=0) + 1,
        "description": description,
        "status": "todo",
        "createdAt": datetime.now().isoformat(),
        "updatedAt": datetime.now().isoformat(),
    }

    tasks.append(task)
    save_tasks()

    print(f"Yay you've added a task successfully. Its ID: {task['id']}")


def list_tasks(status=None):
    found = False
    if not tasks:
        print("No tasks found.")
        return

    for task in tasks:
        print(f"ID: {task['id']}")
        print(f"Description: {task['description']}")
        print(f"Status: {task['status']}")
        print(f"DateMade: {task['createdAt']}")
        print("-------------------")


def update_task(task_id, new_description):
    for task in tasks:
        if task["id"] == task_id:
            task["description"] = new_description
            task["updatedAt"] = datetime.now().isoformat()
            save_tasks()
            print("Yayy! Task updated successfully!")
            return

    print("Task non existent")


def delete_task(task_id):
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            save_tasks()
            print("Task deleted successfully!")
            return

    print("Task not found.")


def update_status(task_id, new_status):
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = new_status
            task["updatedAt"] = datetime.now().isoformat()
            save_tasks()
            print("Task status updated!")
            return

    print("Task not found.")


if len(sys.argv) < 2:
    print("Usage: python task_tracker.py <command>")
    sys.exit()

command = sys.argv[1]

if command == "add":
    if len(sys.argv) < 3:
        print("Please provide a task description.")
    else:
        add_task(sys.argv[2])

elif command == "list":
    list_tasks()

elif command == "update":
    if len(sys.argv) < 4:
        print('Usage: python taskManager.py update <id> "new description"')
    else:
        update_task(int(sys.argv[2]), sys.argv[3])

elif command == "delete":
    if len(sys.argv) < 3:
        print("Please provide a task ID.")
    else:
        delete_task(int(sys.argv[2]))

elif command == "mark-in-progress":
    if len(sys.argv) < 3:
        print("Please provide a task ID.")
    else:
        update_status(int(sys.argv[2]), "in-progress")

elif command == "mark-done":
    if len(sys.argv) < 3:
        print("Please provide a task ID.")
    else:
        update_status(int(sys.argv[2]), "done")

elif command == "list":
    if len(sys.argv) == 2:
        list_tasks()
    else:
        list_tasks(sys.argv[2])

else:
    print("Unknown command.")
