"""
My Very Simple To-Do List Application
Author: yaozhikai
Date: 2025-08-21

This is the minimal version.
Features:
- Add a new task
- View all tasks
- Mark task as completed
- Exit
"""

tasks = []  # store events with dict: {"title": str, "done": bool}


def show_menu():
    print("\n=== To-Do List ===")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Exit")


def add_task():
    title = input("Enter task description: ").strip()
    if title:
        tasks.append({"title": title, "done": False})
        print(f"Task '{title}' added.")
    else:
        print("Task cannot be empty.")


def view_tasks():
    if not tasks:
        print("No tasks yet.")
        return
    print("\nYour Tasks:")
    for idx, task in enumerate(tasks, 1):
        status = "✅" if task["done"] else "❌"
        print(f"{idx}. {task['title']} [{status}]")


def mark_done():
    view_tasks()
    if not tasks:
        return
    try:
        idx = int(input("Enter task number to mark as done: "))
        if 1 <= idx <= len(tasks):
            tasks[idx - 1]["done"] = True
            print(f"Task {idx} marked as done.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


def main():
    while True:
        show_menu()
        choice = input("Choose an option: ").strip()
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            mark_done()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()
