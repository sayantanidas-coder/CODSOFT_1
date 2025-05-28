import json
import os

# File to store tasks
TASK_FILE = "tasks.json"

# Load tasks from file if it exists
def load_tasks():
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, "r") as file:
            data = json.load(file)
            tasks = data.get("tasks", [])
            # Auto-fix: Add empty description if missing
            for task in tasks:
                if "description" not in task:
                    task["description"] = ""
            return tasks, data.get("counter", 1)
    return [], 1

# Save tasks to file 
def save_tasks(tasks, counter):
    with open(TASK_FILE, "w") as file:
        json.dump({"tasks": tasks, "counter": counter}, file, indent=4)

# Add a new task
def add_task(tasks, counter):
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    tasks.append({
        "id": counter,
        "title": title,
        "description": description,
        "completed": False
    })
    print("✅ Task added!")
    return counter + 1

# View all tasks
def view_tasks(tasks):
    if not tasks:
        print("📭 No tasks found.")
    else:
        print("\n📋 Your To-Do List:")
        for task in tasks:
            status = "✔️" if task["completed"] else "❌"
            print(f"ID: {task['id']}")
            print(f"Title: {task['title']}")
            print(f"Description: {task['description']}")
            print(f"Status: {status}")
            print("-" * 40)

# Mark a task as completed
def complete_task(tasks):
    task_id = int(input("Enter task ID to mark as completed: "))
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = True
            print("✅ Task marked as completed.")
            return
    print("⚠️ Task not found.")

# Edit a task's title and/or description
def edit_task(tasks):
    task_id = int(input("Enter task ID to edit: "))
    for task in tasks:
        if task["id"] == task_id:
            new_title = input("Enter new title (leave blank to keep unchanged): ")
            new_description = input("Enter new description (leave blank to keep unchanged): ")
            if new_title:
                task["title"] = new_title
            if new_description:
                task["description"] = new_description
            print("✏️ Task updated.")
            return
    print("⚠️ Task not found.")

# Delete a task
def delete_task(tasks):
    task_id = int(input("Enter task ID to delete: "))
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            print("🗑️ Task deleted.")
            return
    print("⚠️ Task not found.")

# Main menu loop
def main():
    tasks, counter = load_tasks()

    while True:
        print("\n====== TO-DO LIST MENU ======")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Edit Task")
        print("5. Delete Task")
        print("6. Save & Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            counter = add_task(tasks, counter)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            complete_task(tasks)
        elif choice == '4':
            edit_task(tasks)
        elif choice == '5':
            delete_task(tasks)
        elif choice == '6':
            save_tasks(tasks, counter)
            print("💾 Tasks saved. Exiting. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
