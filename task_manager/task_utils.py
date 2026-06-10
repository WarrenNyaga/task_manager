# task_manager/task_utils.py
from .validation import validate_task_title, validate_task_description, validate_due_date

# A list to store the task dictionaries
tasks_list = []

def add_task(title, description, due_date):
    """Validates inputs and adds a new task dictionary to the list."""
    try:
        validate_task_title(title)
        validate_task_description(description)
        validate_due_date(due_date)
        
        new_task = {
            "title": title.strip(),
            "description": description.strip(),
            "due_date": due_date,
            "completed": False
        }
        tasks_list.append(new_task)
        print("Task added successfully")
        return True
    except ValueError as e:
        print(str(e))
        return False

def mark_task_as_complete(title):
    """Finds a task by title and marks it completed."""
    for task in tasks_list:
        if task["title"].lower() == title.strip().lower():
            task["completed"] = True
            print("Task marked as complete")
            return True
    print(f"Error: Task titled '{title}' not found.")
    return False

def view_pending_tasks():
    """Prints out all tasks where completed is False."""
    pending = [t for t in tasks_list if not t["completed"]]
    if not pending:
        print("No pending tasks available.")
        return
    
    print("\n--- Pending Tasks ---")
    for idx, task in enumerate(pending, 1):
        print(f"{idx}. {task['title']} - Due: {task['due_date']}")
        print(f"   Description: {task['description']}\n")

def calculate_progress():
    """Calculates and returns the percentage of completed tasks."""
    total = len(tasks_list)
    if total == 0:
        print("Progress: 0% completed (No tasks created yet).")
        return 0.0
    
    completed_count = sum(1 for t in tasks_list if t["completed"])
    percentage = (completed_count / total) * 100
    print(f"Progress: {percentage:.2f}% completed ({completed_count}/{total} tasks)")
    return percentage