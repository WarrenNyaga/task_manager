from datetime import datetime
from task_manager.validation import validate_task_title, validate_task_description, validate_due_date

# Define tasks list
tasks = []

# Implement add_task function
def add_task(title, description, due_date, tasks=tasks):
    validate_task_title(title)
    validate_task_description(description)
    validate_due_date(due_date)

    task = {
        "title": title.strip(),
        "description": description.strip(),
        "due_date": due_date.strip(),
        "completed": False,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }
    tasks.append(task)
    print("Task added successfully!")
    return task
    
# Implement mark_task_as_complete function
def mark_task_as_complete(index, tasks=tasks):
    if not isinstance(index, int):
        raise ValueError("Index must be an integer.")
    if index < 0 or index >= len(tasks):
        raise IndexError("Task index out of range.")

    tasks[index]["completed"] = True
    print("Task marked as complete!")
    return tasks[index]
    
# Implement view_pending_tasks function
def view_pending_tasks(tasks=tasks):
    pending = [task for task in tasks if not task.get("completed", False)]
    return pending

# Implement calculate_progress function
def calculate_progress(tasks=tasks):
    total = len(tasks)
    if total == 0:
        return 0

    completed_count = sum(1 for task in tasks if task.get("completed", False))
    progress = int((completed_count / total) * 100)
    return progress