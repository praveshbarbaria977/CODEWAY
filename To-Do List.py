import os
import json

# File to store tasks
tasks_file = "tasks.json"

def load_tasks():
    """Load tasks from the file."""
    if os.path.exists(tasks_file):
        with open(tasks_file, "r") as file:
            tasks = json.load(file)
        return tasks
    else:
        return []

def save_tasks(tasks):
    """Save tasks to the file."""
    with open(tasks_file, "w") as file:
        json.dump(tasks, file, indent=2)

def display_tasks(tasks):
    """Display the current tasks."""
    if not tasks:
        print("No tasks found.")
    else:
        print("Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task['title']} - {task['description']}")

def add_task(tasks, title, description):
    """Add a new task to the list."""
    new_task = {"title": title, "description": description, "done": False}
    tasks.append(new_task)
    save_tasks(tasks)
    print("Task added successfully.")

def update_task(tasks, task_index, title, description, done):
    """Update an existing task."""
    if 0 < task_index <= len(tasks):
        task = tasks[task_index - 1]
        task["title"] = title
        task["description"] = description
        task["done"] = done
        save_tasks(tasks)
        print("Task updated successfully.")
    else:
        print("Invalid task index.")

def main():
    # Load tasks from the file
    tasks = load_tasks()

    while True:
        print("\nOptions:")
        print("1. Display tasks")
        print("2. Add a new task")
        print("3. Update a task")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            display_tasks(tasks)
        elif choice == "2":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            add_task(tasks, title, description)
        elif choice == "3":
            display_tasks(tasks)
            task_index = int(input("Enter the task index to update: "))
            title = input("Enter updated task title: ")
            description = input("Enter updated task description: ")
            done = input("Is the task done? (True/False): ").capitalize() == "True"
            update_task(tasks, task_index, title, description, done)
        elif choice == "4":
            print("Quitting the application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
