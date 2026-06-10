# main.py
from task_manager.task_utility import (
    add_task, 
    mark_task_as_complete, 
    view_pending_tasks, 
    calculate_progress
)

def main_menu():
    while True:
        print("\n=============================")
        print("   Task Management System    ")
        print("=============================")
        print("1. Add Task")
        print("2. Mark Task as Complete")
        print("3. View Pending Tasks")
        print("4. Calculate Progress")
        print("5. Exit")
        print("=============================")
        
        choice = input("Enter your choice (1-5): ").strip()
        
        if choice == "1":
            print("\n--- Add a New Task ---")
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            add_task(title, description, due_date)
            
        elif choice == "2":
            print("\n--- Complete a Task ---")
            title = input("Enter the title of the task to complete: ")
            mark_task_as_complete(title)
            
        elif choice == "3":
            view_pending_tasks()
            
        elif choice == "4":
            print("\n--- System Progress ---")
            calculate_progress()
            
        elif choice == "5":
            print("Exiting Task Management System. Goodbye!")
            break
        else:
            print("Invalid selection. Please choose a option between 1 and 5.")

if __name__ == "__main__":
    main_menu()