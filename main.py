from task_manager.task_utils import add_task, mark_task_as_complete, view_pending_tasks, calculate_progress, tasks

# Define the main function
def main():
    while True:
        print("Task Management System")
        print("1. Add Task")
        print("2. Mark Task as Complete")
        print("3. View Pending Tasks")
        print("4. View Progress")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            try:
                add_task(title, description, due_date)
            except ValueError as error:
                print(error)
        elif choice == "2":
            pending = view_pending_tasks()
            if not pending:
                print("No pending tasks available.")
                continue
            print("Pending tasks:")
            pending_indices = [idx for idx, task in enumerate(tasks) if not task.get("completed", False)]
            for display_index, task_index in enumerate(pending_indices):
                task = tasks[task_index]
                print(f"{task_index}: {task['title']} (Due: {task['due_date']})")
            try:
                index = int(input("Enter task index to mark complete: "))
                mark_task_as_complete(index)
            except (ValueError, IndexError) as error:
                print(error)
        elif choice == "3":
            pending = view_pending_tasks()
            if not pending:
                print("No pending tasks.")
            else:
                print("Pending tasks:")
                for idx, task in enumerate(pending):
                    print(f"{idx}: {task['title']} - {task['description']} (Due: {task['due_date']})")
        elif choice == "4":
            progress = calculate_progress()
            print(f"Progress: {progress}%")
        elif choice == "5":
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()