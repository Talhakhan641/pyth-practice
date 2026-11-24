import manager
from manager import TaskManager

manager = TaskManager()
manager.load_tasks()
while True:
    try:
        print("\nTask Manager")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            title = input("Enter task title: ")
            manager.add_task(title)
        elif choice == '2':
            manager.list_tasks()
        elif choice == '3':
            task_id = int(input("Enter task ID to mark as done: "))
            manager.complete_task(task_id)
        elif choice == '4':
            task_id = int(input("Enter task ID to delete: "))
            manager.delete_task(task_id)
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
    
manager.add_task("Learn Python")
manager.add_task("Learn Flask")
manager.add_task("Build a project")

print("\nAll Tasks:")
manager.list_tasks()

manager.complete_task(1)
manager.delete_task(2)

print("\nUpdated Tasks:")
manager.list_tasks() 
