def display_menu():
    """Displays the menu options for the to-do list."""
    print("\n--- To-Do List Menu ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Complete")
    print("4. Delete Task")
    print("5. Exit")

def add_task(tasks):
    """Adds a new task to the list."""
    task = input("Enter the task: ")
    tasks.append({"task": task, "completed": False})
    print(f"Task '{task}' added.")

def view_tasks(tasks):
    """Displays all tasks with their status."""
    if not tasks:
        print("No tasks in the list.")
        return

    print("\n--- Your Tasks ---")
    for i, task_item in enumerate(tasks):
        status = "✓" if task_item["completed"] else " "
        print(f"{i + 1}. [{status}] {task_item['task']}")

def mark_task_complete(tasks):
    """Marks a task as complete."""
    view_tasks(tasks)
    try:
        task_index = int(input("Enter the number of the task to mark as complete: ")) - 1
        if 0 <= task_index < len(tasks):
            tasks[task_index]["completed"] = True
            print(f"Task '{tasks[task_index]['task']}' marked as complete.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def delete_task(tasks):
    """Deletes a task from the list."""
    view_tasks(tasks)
    try:
        task_index = int(input("Enter the number of the task to delete: ")) - 1
        if 0 <= task_index < len(tasks):
            removed_task = tasks.pop(task_index)
            print(f"Task '{removed_task['task']}' deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def main():
    """Main function to run the to-do list application."""
    tasks = []

    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            mark_task_complete(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            print("Exiting the to-do list application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
