tasks = []

def main_menu():
    print("\n" + 5*"_" + "Task manager" + 5*"_")
    print("1. Add task")
    print("2. Show tasks")
    print("3. Remove task")
    print("4. Shutdown task manager")
    
    while True:
        try:
            choice = int(input("\nSelect option (1-4): "))
            if 1 <= choice <= 4:
                return choice
            else:
                print("Please select option 1 to 4")
        except ValueError:
            print("Please select option 1 to 4")

def add_task():
    """
    Adds a new task with name and description to the task list.
    """
    task_name = input("Task title: ")
    if not task_name.strip():
        print("Title cannot be empty.")
        return
    
    task_description = input("Task description: ")
    task = {
        "name": task_name,
        "description": task_description
    }
    
    tasks.append(task)
    print(f"Task '{task_name}' added.")

def show_tasks():
    if not tasks:
        print("There are no tasks yet, please add some.")
    else:
        print("\n" + 5*"_" + "Task manager" + 5*"_")
        for index, task in enumerate(tasks, 1):
            print(f"{index}. {task['name']}")
            print(f"   Description: {task['description'] if task['description'] else '(no description)'}")
            print()

def remove_task():
    if not tasks:
        print("There are no tasks yet, please add some.")
        return
    
    show_tasks()  # We will show the tasks so the user can select them
    
    while True:
        try:
            task_index = int(input("\nEnter number of the task: "))
            if 1 <= task_index <= len(tasks):
                removed_task = tasks.pop(task_index - 1)
                print(f"Task '{removed_task['name']}' was removed.")
                break
            else:
                print(f"Please enter unmber between 1 and {len(tasks)}.")
        except ValueError:
            print(f"Please enter unmber between 1 and {len(tasks)}.")

def shutdown():
    print("Shutting down...")
    exit()

def main():
    print("Please select an option 1 to 4")
    
    while True:
        choice = main_menu()
        
        if choice == 1:
            add_task()
        elif choice == 2:
            show_tasks()
        elif choice == 3:
            remove_task()
        elif choice == 4:
            shutdown()

if __name__ == "__main__":
    main()