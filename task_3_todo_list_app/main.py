# Task 3 – Simple To-Do List App

def show_menu():
    print("\n----- To-Do List Menu -----")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")
    print("---------------------------")

def add_task(tasks):
    task_len = int(input("How many tasks do you want to add? "))
    for i in range(task_len):
        task = input(f"Enter task {i+1}: ").strip().title()
        if task:
            tasks.append(task)
            print(f"Task added: '{task}'")
        else:
            print("Task cannot be empty!")

def view_tasks(tasks):
    print("\n----- Your To-Do List -----")
    if not tasks:
        print("No tasks available.")
    else:
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
    print("---------------------------")

def delete_task(tasks):
    view_tasks(tasks)
    if tasks:
        try:
            choice = int(input("Enter the task number to delete: "))
            if 1 <= choice <= len(tasks):
                removed = tasks.pop(choice - 1)
                print(f"Task deleted: '{removed}'")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

def main():
    tasks = []
    while True:
        show_menu()
        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            print("Exiting... Have a productive day!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
